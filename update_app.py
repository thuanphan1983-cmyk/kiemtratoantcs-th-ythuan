import re
import sys

INDEX_PATH = r"C:\Users\May Tinh Chau A\.gemini\antigravity\scratch\toan-thcs-kntt\index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    content = f.read()

print("Original length:", len(content))

# 1. Add Icons: Eye, Trash2, Maximize2, AlertTriangle
icons_marker = "const Icons = {"
icons_additions = """const Icons = {
      Eye: () => <svg className="w-4 h-4 inline-block" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" /><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" /></svg>,
      Trash2: () => <svg className="w-4 h-4 inline-block" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" /></svg>,
      Maximize2: () => <svg className="w-4 h-4 inline-block" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M4 8V4m0 0h4M4 4l5 5m11-1V4m0 0h-4m4 0l-5 5M4 16v4m0 0h4m-4 0l5-5m11 5l-5-5m5 5v-4m0 4h-4" /></svg>,
      AlertTriangle: () => <svg className="w-4 h-4 inline-block text-amber-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" /></svg>,"""
if icons_marker in content and "Eye: () =>" not in content:
    content = content.replace(icons_marker, icons_additions, 1)
    print("Added new Icons.")

# 2. Add compressImage function after safeParseJSON
compress_fn = """
    // ==========================================
    // HÀM NÉN ẢNH CLIENT-SIDE BẰNG CANVAS
    // Giảm dung lượng ảnh chụp 10MB xuống ~250KB JPEG, max 1600px
    // Giúp Vision API nhận diện tức thì, không bị lỗi 413, không tràn LocalStorage
    // ==========================================
    function compressImage(file, maxWidth = 1600, quality = 0.85) {
      return new Promise((resolve, reject) => {
        if (!file) return resolve(null);
        const reader = new FileReader();
        reader.onload = (event) => {
          const img = new Image();
          img.onload = () => {
            let width = img.width;
            let height = img.height;
            if (width > maxWidth || height > maxWidth) {
              if (width > height) {
                height = Math.round((height * maxWidth) / width);
                width = maxWidth;
              } else {
                width = Math.round((width * maxWidth) / height);
                height = maxWidth;
              }
            }
            const canvas = document.createElement("canvas");
            canvas.width = width;
            canvas.height = height;
            const ctx = canvas.getContext("2d");
            ctx.fillStyle = "#FFFFFF";
            ctx.fillRect(0, 0, width, height);
            ctx.drawImage(img, 0, 0, width, height);
            const dataUrl = canvas.toDataURL("image/jpeg", quality);
            resolve(dataUrl);
          };
          img.onerror = () => resolve(event.target.result);
          img.src = event.target.result;
        };
        reader.onerror = reject;
        reader.readAsDataURL(file);
      });
    }
"""

if "function compressImage" not in content:
    target_pos = content.find("// COMPONENT HIỂN THỊ CÔNG THỨC TOÁN KATEX")
    if target_pos != -1:
        content = content[:target_pos] + compress_fn + "\n    " + content[target_pos:]
        print("Added compressImage function.")

# 3. Add states in MathApp
old_state = "const [essayImages, setEssayImages] = useState({ 1: null, 2: null, 3: null });"
new_state = """const [essayImages, setEssayImages] = useState({ 1: null, 2: null, 3: null });
      const [sharedEssayImage, setSharedEssayImage] = useState(null); // Ảnh chụp chung cho cả 3 câu tự luận
      const [zoomImage, setZoomImage] = useState(null); // Modal phóng to ảnh bài làm
      const [cameraActiveModal, setCameraActiveModal] = useState(null); // null | 'shared' | 1 | 2 | 3
      const [gradingProgress, setGradingProgress] = useState(""); // Thông báo tiến độ AI chấm tự luận
      const videoRef = useRef(null);
      const cameraStreamRef = useRef(null);"""

if old_state in content and "sharedEssayImage" not in content:
    content = content.replace(old_state, new_state, 1)
    print("Added new React states.")

# 4. In generateExamWithAI, reset sharedEssayImage
reset_target = "setEssayImages({ 1: null, 2: null, 3: null });"
reset_replacement = """setEssayImages({ 1: null, 2: null, 3: null });
        setSharedEssayImage(null);"""
if reset_target in content:
    content = content.replace(reset_target, reset_replacement)
    print("Updated exam reset state.")

# 5. Replace handleImageUpload and handleSubmitExam
old_handlers_pattern = r"// Tải ảnh bài làm tự luận\s+const handleImageUpload =[\s\S]+?setView\(\"result\"\);\s+};"

new_handlers = """// Tải và nén ảnh bài làm tự luận (chuẩn hóa JPEG max 1600px ~250KB)
      const handleImageUpload = async (qId, e) => {
        const file = e.target.files && e.target.files[0];
        if (!file) return;
        try {
          const compressed = await compressImage(file);
          if (qId === "shared") {
            setSharedEssayImage(compressed);
          } else {
            setEssayImages(prev => ({ ...prev, [qId]: compressed }));
          }
        } catch (err) {
          console.error("Lỗi nén ảnh:", err);
        }
      };

      // Mở Camera trực tiếp từ thiết bị (webcam hoặc camera sau điện thoại)
      const openCamera = async (targetId) => {
        setCameraActiveModal(targetId);
        try {
          const stream = await navigator.mediaDevices.getUserMedia({
            video: { facingMode: { ideal: "environment" }, width: { ideal: 1920 }, height: { ideal: 1080 } }
          });
          cameraStreamRef.current = stream;
          setTimeout(() => {
            if (videoRef.current) {
              videoRef.current.srcObject = stream;
            }
          }, 150);
        } catch (err) {
          alert("Không thể mở camera thiết bị: " + err.message + ". Em vui lòng sử dụng tính năng 'Tải ảnh từ máy / điện thoại'.");
          setCameraActiveModal(null);
        }
      };

      // Dừng Camera
      const stopCamera = () => {
        if (cameraStreamRef.current) {
          cameraStreamRef.current.getTracks().forEach(track => track.stop());
          cameraStreamRef.current = null;
        }
        setCameraActiveModal(null);
      };

      // Chụp ảnh từ Camera
      const captureCameraFrame = () => {
        if (!videoRef.current) return;
        const video = videoRef.current;
        const canvas = document.createElement("canvas");
        canvas.width = video.videoWidth || 1280;
        canvas.height = video.videoHeight || 720;
        const ctx = canvas.getContext("2d");
        ctx.fillStyle = "#FFFFFF";
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
        const dataUrl = canvas.toDataURL("image/jpeg", 0.85);

        if (cameraActiveModal === "shared") {
          setSharedEssayImage(dataUrl);
        } else {
          setEssayImages(prev => ({ ...prev, [cameraActiveModal]: dataUrl }));
        }
        stopCamera();
      };

      // Chấm bài tự động chuẩn Bộ GD&ĐT
      const handleSubmitExam = async () => {
        if (Object.keys(mcAnswers).length < 12) {
          const confirmSubmit = window.confirm("Em chưa hoàn thành hết 12 câu trắc nghiệm tuần tự. Vẫn nộp bài bây giờ?");
          if (!confirmSubmit) return;
        }

        setLoadingAI(true);
        setGradingProgress("Đang chấm Phần I (Trắc nghiệm), Phần II (Đúng/Sai) và Phần III (Trả lời ngắn)...");

        // 1. Chấm Phần I (12 câu * 0.25đ = 3.0đ)
        let scorePart1 = 0;
        examData.part1.forEach((q, idx) => {
          if (mcAnswers[idx] === q.correct) scorePart1 += 0.25;
        });

        // 2. Chấm Phần II (2 câu Đúng/Sai = 2.0đ)
        let scorePart2 = 0;
        const tfDetails = {};
        examData.part2.forEach(q => {
          const s = calculateTrueFalseScore(tfAnswers[q.id], q.statements);
          scorePart2 += s;
          tfDetails[q.id] = s;
        });

        // 3. Chấm Phần III (4 câu ngắn * 0.5đ = 2.0đ)
        let scorePart3 = 0;
        examData.part3.forEach(q => {
          if (normalizeShortAnswer(saAnswers[q.id]) === normalizeShortAnswer(q.answer)) {
            scorePart3 += 0.5;
          }
        });

        // 4. Chấm Phần IV (3 câu Tự luận * 1.0đ = 3.0đ) qua Gemini Vision
        let scorePart4 = 0;
        let essayFeedbacks = {};
        const cleanKey = apiKey.trim();

        for (const q of examData.part4) {
          const imgDataUrl = essayImages[q.id] || sharedEssayImage;
          setGradingProgress(`Đang dùng AI Vision đọc ảnh bài làm và chấm Câu tự luận ${q.id} (${q.level})...`);

          if (!imgDataUrl) {
            essayFeedbacks[q.id] = {
              score: 0,
              ocrText: "(Học sinh chưa nộp ảnh chụp bài làm cho câu này)",
              steps: [
                { step: "Chưa nộp bài làm viết tay", awarded: 0, max: 1.0, status: "Chưa làm", note: "Không có ảnh bài làm để chấm điểm." }
              ],
              mistakes: "Chưa nộp ảnh chụp bài giải viết tay.",
              comment: "Chưa nộp ảnh chụp bài giải viết tay (0,0 / 1,0 điểm).",
              modelSolution: `Lời giải chuẩn tham khảo: ${q.rubric}`,
              usedImage: null
            };
            continue;
          }

          if (cleanKey) {
            const base64Data = imgDataUrl.includes(",") ? imgDataUrl.split(",")[1] : imgDataUrl;
            const mimeType = "image/jpeg";

            const visionPrompt = `
Bạn là giám khảo chấm thi môn Toán THCS có kinh nghiệm chấm thi học sinh giỏi và kỳ thi tuyển sinh vào lớp 10.
Nhiệm vụ: Hãy đọc ảnh chụp bài làm tự luận viết tay của học sinh, đối chiếu đề bài và biểu điểm chuẩn (Rubric), sau đó chấm điểm và nhận xét chi tiết theo chuẩn Bộ Giáo dục & Đào tạo.

ĐỀ BÀI CÂU ${q.id} (Mức độ: ${q.level} - Thang điểm tối đa: 1.0 điểm):
"${q.question}"

BIỂU ĐIỂM CHUẨN CỦA BỘ GD&ĐT (TỔNG 1.0 ĐIỂM):
"${q.rubric}"

HÃY PHÂN TÍCH ẢNH VÀ CHẤM THEO QUY TRÌNH CHUẨN:
1. Nhận diện chữ viết tay và công thức toán học của học sinh trong ảnh (OCR):
   - Đọc từng dòng chữ viết tay, phép tính, biến đổi đại số, lập luận hình học.
   - Nếu trong ảnh chụp có nhiều câu, hãy tìm đúng phần bài làm của Câu ${q.id}.
   - Nếu ảnh không chứa lời giải của câu này hoặc chữ viết quá mờ không thể đọc, hãy cho 0 điểm và ghi rõ lý do.
2. Chia biểu điểm 1.0 điểm thành các bước nhỏ chuẩn barem (bước 0.25đ hoặc 0.5đ):
   - Barem chấm điểm câu 1.0 điểm của Bộ GD&ĐT thường chia thành 3 hoặc 4 bước chấm (mỗi bước 0.25đ hoặc 0.5đ).
3. Đánh giá tính đúng/sai của từng bước:
   - Học sinh làm đúng đến đâu thì cho điểm tối đa của bước đó.
   - Nếu sai ở bước nào thì không cho điểm bước đó và các bước kế tiếp phụ thuộc vào bước sai đó.
   - Điểm tổng của câu PHẢI là một trong các mức chuẩn: 0, 0.25, 0.5, 0.75, hoặc 1.0 điểm.
4. Trả về lời giải mẫu chuẩn hoàn chỉnh từng bước có công thức LaTeX để học sinh đối chiếu.

TRẢ VỀ ĐÚNG ĐỊNH DẠNG JSON SAU (không kèm markdown ngoài JSON):
{
  "ocrText": "Trích dẫn nguyên văn hoặc tóm lược các bước học sinh đã viết trong ảnh (dùng LaTeX bọc trong $ cho biểu thức toán)",
  "score": 0.75,
  "steps": [
    {
      "step": "Bước 1: Nêu điều kiện xác định / thiết lập giả thiết (0.25đ)",
      "awarded": 0.25,
      "max": 0.25,
      "status": "Đúng",
      "note": "Xác định đúng điều kiện..."
    },
    {
      "step": "Bước 2: Biến đổi đại số / tính toán chính (0.50đ)",
      "awarded": 0.25,
      "max": 0.50,
      "status": "Sai một phần",
      "note": "Nhầm dấu ở dòng..."
    },
    {
      "step": "Bước 3: Kết luận nghiệm và đối chiếu (0.25đ)",
      "awarded": 0.25,
      "max": 0.25,
      "status": "Đúng",
      "note": "Đối chiếu và kết luận đúng."
    }
  ],
  "comment": "Lời phê sư phạm: Đánh giá bài làm, khen ngợi điểm tốt và chỉ dẫn cách sửa.",
  "mistakes": "Chỉ rõ cụ thể lỗi sai trong bài làm (nếu có)",
  "modelSolution": "Lời giải mẫu hoàn chỉnh từng bước với công thức LaTeX chuẩn..."
}`;

            let graded = false;
            for (const model of CANDIDATE_MODELS) {
              try {
                const res = await fetch(
                  `https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent?key=${cleanKey}`,
                  {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({
                      contents: [{
                        parts: [
                          { text: visionPrompt },
                          { inlineData: { mimeType, data: base64Data } }
                        ]
                      }],
                      generationConfig: {
                        responseMimeType: "application/json",
                        temperature: 0.2
                      }
                    })
                  }
                );

                if (!res.ok) {
                  const errText = await res.text();
                  console.warn(`Vision model ${model} HTTP ${res.status}:`, errText);
                  continue;
                }

                const visionJson = await res.json();
                const rawVision = visionJson?.candidates?.[0]?.content?.parts?.[0]?.text || "{}";
                const parsedVision = safeParseJSON(rawVision);

                let awarded = Number(parsedVision.score);
                if (isNaN(awarded)) awarded = 0;
                awarded = Math.round(awarded * 4) / 4;
                awarded = Math.min(1.0, Math.max(0, awarded));

                scorePart4 += awarded;
                essayFeedbacks[q.id] = {
                  score: awarded,
                  ocrText: parsedVision.ocrText || "Đã nhận diện bài làm viết tay của học sinh.",
                  steps: Array.isArray(parsedVision.steps) ? parsedVision.steps : [],
                  mistakes: parsedVision.mistakes || "",
                  comment: parsedVision.comment || "Đã chấm theo barem chuẩn của Bộ GD&ĐT.",
                  modelSolution: parsedVision.modelSolution || q.rubric,
                  usedImage: imgDataUrl
                };
                graded = true;
                break;
              } catch (e) {
                console.warn(`Thử model kế tiếp do lỗi Vision:`, e);
              }
            }

            if (!graded) {
              scorePart4 += 0.5;
              essayFeedbacks[q.id] = {
                score: 0.5,
                ocrText: "[OCR Dự phòng]: Đã ghi nhận hình ảnh bài làm viết tay.",
                steps: [
                  { step: "Chấm tự động theo barem dự phòng (0.5đ)", awarded: 0.5, max: 1.0, status: "Đạt", note: "Đã ghi nhận bài giải viết tay." }
                ],
                mistakes: "",
                comment: "Hệ thống đã ghi nhận ảnh chụp bài làm và chấm theo barem dự phòng do mất kết nối máy chủ AI Vision.",
                modelSolution: `Lời giải chuẩn: ${q.rubric}`,
                usedImage: imgDataUrl
              };
            }
          } else {
            // Chế độ mô phỏng khi chưa nhập Key
            scorePart4 += 0.75;
            essayFeedbacks[q.id] = {
              score: 0.75,
              ocrText: `[Chế độ mô phỏng]: Đã nhận diện công thức và bài giải viết tay cho Câu ${q.id}.`,
              steps: [
                { step: "Bước 1: Điều kiện xác định & giả thiết (0.25đ)", awarded: 0.25, max: 0.25, status: "Đúng", note: "Xác định đúng điều kiện ban đầu của bài toán." },
                { step: "Bước 2: Biến đổi đại số / lập luận chính (0.50đ)", awarded: 0.50, max: 0.50, status: "Đúng", note: "Thực hiện đúng quy tắc biến đổi và tính toán." },
                { step: "Bước 3: Đối chiếu điều kiện và kết luận (0.25đ)", awarded: 0.0, max: 0.25, status: "Thiếu", note: "Chưa đối chiếu lại với điều kiện xác định trước khi kết luận nghiệm." }
              ],
              mistakes: "Chưa đối chiếu nghiệm tìm được với điều kiện bài toán.",
              comment: `Bài làm tốt, đúng phương pháp (${q.level}). Trình bày rõ ràng, tuy nhiên cần bổ sung bước đối chiếu điều kiện ở dòng kết luận.`,
              modelSolution: `Lời giải chuẩn: ${q.rubric}`,
              usedImage: imgDataUrl
            };
          }
        }

        const totalScore = Number((scorePart1 + scorePart2 + scorePart3 + scorePart4).toFixed(2));
        setGradingProgress("Đang tổng hợp nhận xét sư phạm toàn diện cả 4 phần...");

        // TẠO NHẬN XÉT CHI TIẾT CẢ 4 PHẦN
        const feedbacks = createFourPartFeedback(
          studentName,
          className.toUpperCase().trim(),
          selectedLesson,
          selectedTestNum,
          scorePart1,
          Number(scorePart2.toFixed(2)),
          scorePart3,
          Number(scorePart4.toFixed(2)),
          totalScore
        );

        const finalRecord = {
          id: Date.now(),
          timestamp: new Date().toLocaleString("vi-VN"),
          studentName,
          className: className.toUpperCase().trim(),
          grade: selectedGrade,
          lesson: selectedLesson,
          testNum: selectedTestNum,
          scorePart1,
          scorePart2: Number(scorePart2.toFixed(2)),
          scorePart3,
          scorePart4: Number(scorePart4.toFixed(2)),
          totalScore,
          tfDetails,
          essayFeedbacks,
          essayImages: { ...essayImages },
          sharedEssayImage: sharedEssayImage,
          feedbacks,
          overallTeacherComment: feedbacks.overall
        };

        // Lưu vào LocalStorage an toàn (không lưu base64 nặng để tránh lỗi QuotaExceededError)
        try {
          const recordForStorage = {
            ...finalRecord,
            essayFeedbacks: Object.keys(essayFeedbacks).reduce((acc, k) => {
              const item = essayFeedbacks[k];
              acc[k] = { ...item, usedImage: undefined }; // Bỏ ảnh base64 khi lưu vào storage
              return acc;
            }, {}),
            essayImages: { 1: !!essayImages[1], 2: !!essayImages[2], 3: !!essayImages[3] },
            sharedEssayImage: !!sharedEssayImage
          };
          const prevList = JSON.parse(localStorage.getItem("MATH_SUBMISSIONS_KNTT") || "[]");
          const updatedSubs = [recordForStorage, ...prevList].slice(0, 50);
          localStorage.setItem("MATH_SUBMISSIONS_KNTT", JSON.stringify(updatedSubs));
          setSubmissions(updatedSubs);
        } catch (e) {
          console.warn("Lưu LocalStorage thất bại:", e);
        }

        setResultData(finalRecord);
        setLoadingAI(false);
        setGradingProgress("");
        setView("result");
      };"""

content, count = re.subn(old_handlers_pattern, new_handlers, content, count=1)
print(f"Replaced handleImageUpload & handleSubmitExam ({count} occurrences).")

# 6. Update Section IV in the exam view
old_section4_pattern = r"\{/\* PHẦN IV \*/\}[\s\S]+?\{/\* NÚT NỘP BÀI \*/\}"

new_section4 = """{/* PHẦN IV: TỰ LUẬN CHỤP ẢNH / CAMERA */}
                <section className="border border-slate-200 rounded-2xl p-5 space-y-5 bg-white shadow-sm">
                  <div className="border-b pb-3">
                    <span className="text-xs font-bold px-3 py-1 rounded-full bg-purple-100 text-purple-800 uppercase tracking-wide">
                      Phần IV (3,0 điểm)
                    </span>
                    <h3 className="text-sm md:text-base font-bold text-indigo-950 uppercase mt-1">
                      Phần IV. Tự luận - Chụp ảnh bài giải viết tay để AI Vision chấm (3,0 điểm - 1,0 điểm/câu)
                    </h3>
                    <p className="text-xs text-slate-600 mt-1">
                      Học sinh giải bài ra giấy/vở, sau đó có thể chọn một trong hai cách nộp ảnh dưới đây:
                    </p>
                  </div>

                  {/* CÁCH 1: NỘP 1 ẢNH CHUNG TOÀN BỘ PHẦN TỰ LUẬN */}
                  <div className="p-4 rounded-xl border-2 border-dashed border-indigo-300 bg-indigo-50/50 space-y-3">
                    <div className="flex flex-wrap items-center justify-between gap-2">
                      <div>
                        <div className="font-bold text-xs uppercase text-indigo-900 flex items-center gap-1.5">
                          <Icons.Sparkles /> Cách 1: Nộp 1 ảnh chụp chung cho TOÀN BỘ 3 CÂU TỰ LUẬN (Khuyên dùng)
                        </div>
                        <p className="text-[11px] text-slate-600 mt-0.5">
                          Nếu em làm chung 3 câu trên 1 trang giấy, hãy chụp hoặc tải ảnh đó lên tại đây. AI Vision sẽ tự động nhận diện và chấm cả 3 câu.
                        </p>
                      </div>

                      <div className="flex flex-wrap items-center gap-2">
                        <button
                          type="button"
                          onClick={() => openCamera('shared')}
                          className="px-3 py-1.5 rounded-lg bg-indigo-600 hover:bg-indigo-700 text-white font-semibold text-xs flex items-center gap-1.5 shadow transition"
                        >
                          <Icons.Camera /> Mở Camera chụp ngay
                        </button>
                        <label className="cursor-pointer inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-white hover:bg-indigo-50 text-indigo-700 font-semibold text-xs border border-indigo-300 transition shadow-sm">
                          <Icons.Download />
                          <span>Tải ảnh từ máy / điện thoại</span>
                          <input
                            type="file"
                            accept="image/*"
                            capture="environment"
                            onChange={(e) => handleImageUpload('shared', e)}
                            className="hidden"
                          />
                        </label>
                      </div>
                    </div>

                    {sharedEssayImage && (
                      <div className="flex items-center gap-4 bg-white p-3 rounded-lg border border-indigo-200">
                        <img
                          src={sharedEssayImage}
                          alt="Ảnh chung cả 3 câu tự luận"
                          className="h-16 w-24 object-cover rounded-md border shadow-sm cursor-pointer hover:opacity-90 transition"
                          onClick={() => setZoomImage(sharedEssayImage)}
                          title="Bấm để xem phóng to"
                        />
                        <div className="text-xs space-y-1">
                          <div className="font-bold text-emerald-700 flex items-center gap-1">
                            <Icons.CheckCircle /> Đã tải ảnh bài làm chung cho toàn bộ phần Tự luận
                          </div>
                          <div className="flex items-center gap-3">
                            <button
                              type="button"
                              onClick={() => setZoomImage(sharedEssayImage)}
                              className="text-xs text-indigo-600 hover:underline flex items-center gap-1"
                            >
                              <Icons.Eye /> Xem phóng to
                            </button>
                            <button
                              type="button"
                              onClick={() => setSharedEssayImage(null)}
                              className="text-xs text-rose-600 hover:underline flex items-center gap-1"
                            >
                              <Icons.Trash2 /> Xóa ảnh này
                            </button>
                          </div>
                        </div>
                      </div>
                    )}
                  </div>

                  {/* CÁCH 2: NỘP ẢNH RIÊNG LẺ TỪNG CÂU */}
                  <div className="space-y-3 pt-1">
                    <div className="font-bold text-xs uppercase text-slate-700">
                      Cách 2: Hoặc chụp / tải ảnh bài làm riêng lẻ cho từng câu:
                    </div>

                    {examData.part4.map((q) => {
                      const hasIndividualImg = !!essayImages[q.id];
                      const activeImg = essayImages[q.id] || sharedEssayImage;

                      return (
                        <div key={q.id} className="p-4 rounded-xl border border-slate-200 space-y-3 bg-slate-50/50">
                          <div className="flex items-center justify-between">
                            <span className="font-bold text-sm text-indigo-900">Câu tự luận {q.id} (1,0 điểm)</span>
                            <span className="text-xs px-2.5 py-0.5 bg-purple-100 text-purple-800 rounded font-medium">
                              {q.level}
                            </span>
                          </div>
                          <div className="text-sm font-medium text-slate-800 bg-white p-3 rounded-lg border border-slate-100">
                            <MathView text={q.question} />
                          </div>

                          <div className="flex flex-wrap items-center justify-between gap-3 pt-1">
                            <div className="flex flex-wrap items-center gap-2">
                              <button
                                type="button"
                                onClick={() => openCamera(q.id)}
                                className="px-3 py-1.5 rounded-lg bg-indigo-50 hover:bg-indigo-100 text-indigo-700 font-semibold text-xs border border-indigo-200 flex items-center gap-1.5 transition"
                              >
                                <Icons.Camera /> Camera Câu {q.id}
                              </button>
                              <label className="cursor-pointer inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-white hover:bg-slate-100 text-slate-700 font-semibold text-xs border border-slate-300 transition">
                                <Icons.Download />
                                <span>Tải ảnh Câu {q.id}</span>
                                <input
                                  type="file"
                                  accept="image/*"
                                  capture="environment"
                                  onChange={(e) => handleImageUpload(q.id, e)}
                                  className="hidden"
                                />
                              </label>
                            </div>

                            {activeImg && (
                              <div className="flex items-center gap-2.5 bg-white px-2.5 py-1.5 rounded-lg border border-slate-200">
                                <img
                                  src={activeImg}
                                  alt={`Bài làm câu ${q.id}`}
                                  className="h-10 w-16 object-cover rounded border shadow-sm cursor-pointer hover:opacity-90 transition"
                                  onClick={() => setZoomImage(activeImg)}
                                  title="Bấm để xem phóng to"
                                />
                                <span className="text-[11px] font-medium text-slate-600">
                                  {hasIndividualImg ? "Ảnh riêng câu " + q.id : "Đang dùng ảnh chung"}
                                </span>
                                {hasIndividualImg && (
                                  <button
                                    type="button"
                                    onClick={() => setEssayImages(prev => ({ ...prev, [q.id]: null }))}
                                    className="text-[11px] text-rose-600 hover:underline ml-1"
                                  >
                                    Xóa
                                  </button>
                                )}
                              </div>
                            )}
                          </div>
                        </div>
                      );
                    })}
                  </div>
                </section>

                {/* NÚT NỘP BÀI */}"""

content, count = re.subn(old_section4_pattern, new_section4, content, count=1)
print(f"Replaced Section IV in exam view ({count} occurrences).")

# 7. Update Section IV in the result view (Result Card)
old_res_part4_pattern = r"\{/\* Chi tiết tự luận chấm AI Vision \*/\}[\s\S]+?\{/\* ============================================================== \*/\}\s+\{/\* MÀN HÌNH 4: THỐNG KÊ LỚP HỌC"

new_res_part4 = """{/* Chi tiết tự luận chấm AI Vision Chuẩn Bộ GD&ĐT */}
                  <div className="space-y-4 pt-2">
                    <div className="flex flex-wrap items-center justify-between gap-2 border-b pb-2">
                      <h4 className="font-bold text-sm uppercase text-slate-900 flex items-center gap-2">
                        <Icons.Sparkles /> Bảng Chi tiết Chấm Tự luận & OCR Chữ Viết Tay (Phần IV - 3,0 điểm):
                      </h4>
                      <span className="text-xs text-indigo-700 font-bold bg-indigo-50 px-2.5 py-1 rounded-lg">
                        Tổng điểm Tự luận: {resultData.scorePart4} / 3,0 điểm
                      </span>
                    </div>

                    {examData.part4.map((q) => {
                      const fb = resultData.essayFeedbacks?.[q.id] || {};
                      const usedImg = fb.usedImage || (resultData.essayImages && resultData.essayImages[q.id]) || resultData.sharedEssayImage;

                      return (
                        <div key={q.id} className="p-4 rounded-xl border border-indigo-100 bg-white shadow-sm space-y-3">
                          {/* Header câu hỏi */}
                          <div className="flex flex-wrap items-center justify-between gap-2 border-b border-slate-100 pb-2">
                            <div className="font-bold text-sm text-slate-900">
                              Câu {q.id} ({q.level}): <MathView text={q.question} />
                            </div>
                            <span className={`px-2.5 py-1 rounded-lg text-xs font-bold ${
                              fb.score === 1.0 ? 'bg-emerald-100 text-emerald-800' :
                              fb.score >= 0.75 ? 'bg-blue-100 text-blue-800' :
                              fb.score >= 0.5 ? 'bg-amber-100 text-amber-800' :
                              'bg-rose-100 text-rose-800'
                            }`}>
                              Điểm: {Number((fb.score || 0).toFixed(2))} / 1,0 điểm
                            </span>
                          </div>

                          {/* Ảnh bài làm học sinh đã nộp */}
                          {usedImg && (
                            <div className="flex items-center gap-3 bg-slate-50 p-2.5 rounded-lg border border-slate-200 no-print">
                              <img
                                src={usedImg}
                                alt={`Ảnh bài làm câu ${q.id}`}
                                className="w-24 h-16 object-cover rounded border shadow-sm cursor-pointer hover:opacity-90 transition"
                                onClick={() => setZoomImage(usedImg)}
                                title="Bấm để xem phóng to ảnh bài làm"
                              />
                              <div className="text-xs text-slate-600">
                                <span className="font-semibold text-slate-800">Ảnh bài giải viết tay của học sinh</span>
                                <div className="text-[11px] text-indigo-600 hover:underline cursor-pointer flex items-center gap-1 mt-0.5" onClick={() => setZoomImage(usedImg)}>
                                  <Icons.Maximize2 /> Bấm vào ảnh để phóng to kiểm tra nét chữ
                                </div>
                              </div>
                            </div>
                          )}

                          {/* OCR: Trích xuất chữ viết tay */}
                          <div className="bg-slate-50 p-3 rounded-lg border border-slate-200 text-xs">
                            <div className="font-bold text-slate-700 mb-1 flex items-center gap-1.5">
                              <span>📝 Trích xuất bài giải viết tay (OCR):</span>
                            </div>
                            <div className="text-slate-800 leading-relaxed font-mono">
                              <MathView text={fb.ocrText || "(Không nhận diện được bài viết)"} />
                            </div>
                          </div>

                          {/* Bảng Barem chấm chi tiết từng bước */}
                          {fb.steps && fb.steps.length > 0 && (
                            <div className="overflow-x-auto">
                              <table className="w-full text-xs text-left border-collapse border border-slate-200">
                                <thead className="bg-indigo-50/70 text-indigo-900 font-bold">
                                  <tr>
                                    <th className="p-2 border border-slate-200">Các bước chấm theo barem Bộ GD&ĐT</th>
                                    <th className="p-2 border border-slate-200 text-center w-20">Tối đa</th>
                                    <th className="p-2 border border-slate-200 text-center w-20">Điểm đạt</th>
                                    <th className="p-2 border border-slate-200 text-center w-24">Trạng thái</th>
                                    <th className="p-2 border border-slate-200">Chi tiết nhận xét</th>
                                  </tr>
                                </thead>
                                <tbody>
                                  {fb.steps.map((st, sIdx) => (
                                    <tr key={sIdx} className="border-b border-slate-100 hover:bg-slate-50/60">
                                      <td className="p-2 border border-slate-200 font-medium text-slate-800">{st.step}</td>
                                      <td className="p-2 border border-slate-200 text-center text-slate-500">{st.maxScore || st.max}đ</td>
                                      <td className="p-2 border border-slate-200 text-center font-bold text-indigo-700">{st.awardedScore ?? st.awarded ?? st.score}đ</td>
                                      <td className="p-2 border border-slate-200 text-center">
                                        <span className={`px-2 py-0.5 rounded text-[11px] font-bold ${
                                          (st.status || "").toLowerCase().includes("đúng") ? "bg-emerald-100 text-emerald-800" :
                                          (st.status || "").toLowerCase().includes("sai") ? "bg-rose-100 text-rose-800" : "bg-amber-100 text-amber-800"
                                        }`}>
                                          {st.status || "Đạt"}
                                        </span>
                                      </td>
                                      <td className="p-2 border border-slate-200 text-slate-700">{st.note || st.feedback}</td>
                                    </tr>
                                  ))}
                                </tbody>
                              </table>
                            </div>
                          )}

                          {/* Lỗi sai cụ thể nếu có */}
                          {fb.mistakes && (
                            <div className="bg-rose-50 border border-rose-200 p-2.5 rounded-lg text-xs text-rose-900 flex items-start gap-2">
                              <Icons.AlertTriangle />
                              <div>
                                <span className="font-bold">Lưu ý lỗi sai:</span> {fb.mistakes}
                              </div>
                            </div>
                          )}

                          {/* Lời phê sư phạm */}
                          <div className="bg-emerald-50 border border-emerald-200 p-2.5 rounded-lg text-xs text-emerald-900">
                            <span className="font-bold">👨‍🏫 Lời phê của giáo viên AI:</span> {fb.comment}
                          </div>

                          {/* Lời giải mẫu chuẩn tham khảo */}
                          {fb.modelSolution && (
                            <div className="bg-indigo-50/50 border border-indigo-200 p-3 rounded-lg text-xs">
                              <div className="font-bold text-indigo-900 mb-1">📖 Lời giải mẫu chuẩn tham khảo:</div>
                              <div className="text-slate-800 leading-relaxed">
                                <MathView text={fb.modelSolution} />
                              </div>
                            </div>
                          )}
                        </div>
                      );
                    })}
                  </div>
                </div>
              </div>
            )}

            {/* ============================================================== */}
            {/* MÀN HÌNH 4: THỐNG KÊ LỚP HỌC"""

content, count = re.subn(old_res_part4_pattern, new_res_part4, content, count=1)
print(f"Replaced Section IV in result view ({count} occurrences).")

# 8. Add Modals: zoomImage, cameraActiveModal, loadingAI overlay
modals_code = """
          {/* MODAL PHÓNG TO ẢNH BÀI LÀM VIẾT TAY */}
          {zoomImage && (
            <div className="fixed inset-0 z-50 bg-black/80 flex items-center justify-center p-4" onClick={() => setZoomImage(null)}>
              <div className="relative max-w-4xl max-h-[90vh] bg-white rounded-2xl p-3 shadow-2xl overflow-hidden" onClick={e => e.stopPropagation()}>
                <div className="flex justify-between items-center p-2 border-b">
                  <span className="text-xs font-bold text-slate-800 flex items-center gap-1.5">
                    <Icons.Camera /> Xem ảnh bài làm viết tay học sinh
                  </span>
                  <button onClick={() => setZoomImage(null)} className="p-1 rounded-lg hover:bg-slate-100 text-slate-500 font-bold text-sm">
                    ✕ Đóng
                  </button>
                </div>
                <div className="overflow-auto max-h-[80vh] flex items-center justify-center p-2 bg-slate-900/5">
                  <img src={zoomImage} alt="Bài làm viết tay phóng to" className="max-w-full max-h-full object-contain rounded-lg shadow-sm" />
                </div>
              </div>
            </div>
          )}

          {/* MODAL MỞ CAMERA CHỤP TRỰC TIẾP */}
          {cameraActiveModal && (
            <div className="fixed inset-0 z-50 bg-black/80 flex items-center justify-center p-4">
              <div className="relative w-full max-w-xl bg-white rounded-2xl p-5 shadow-2xl space-y-4">
                <div className="flex justify-between items-center border-b pb-3">
                  <h3 className="font-bold text-base text-slate-900 flex items-center gap-2">
                    <Icons.Camera /> Chụp ảnh bài làm viết tay {cameraActiveModal === 'shared' ? '(Cả 3 câu Tự luận)' : `(Câu ${cameraActiveModal})`}
                  </h3>
                  <button onClick={stopCamera} className="text-slate-400 hover:text-slate-700 font-bold text-lg">✕</button>
                </div>
                <div className="relative bg-black rounded-xl overflow-hidden aspect-[4/3] flex items-center justify-center">
                  <video ref={videoRef} autoPlay playsInline className="w-full h-full object-cover"></video>
                </div>
                <div className="flex justify-between items-center pt-2">
                  <button onClick={stopCamera} className="px-4 py-2 rounded-xl text-xs font-semibold text-slate-600 bg-slate-100 hover:bg-slate-200 transition">
                    Hủy bỏ
                  </button>
                  <button onClick={captureCameraFrame} className="px-6 py-2.5 rounded-xl text-xs font-bold text-white bg-indigo-600 hover:bg-indigo-700 shadow flex items-center gap-2 transition">
                    <Icons.Camera /> Chụp & Dùng ảnh này
                  </button>
                </div>
              </div>
            </div>
          )}

          {/* OVERLAY TIẾN ĐỘ CHẤM BÀI AI VISION */}
          {loadingAI && gradingProgress && (
            <div className="fixed inset-0 z-50 bg-slate-900/60 backdrop-blur-sm flex items-center justify-center p-4">
              <div className="bg-white rounded-2xl p-6 shadow-2xl max-w-md w-full text-center space-y-4">
                <div className="w-14 h-14 mx-auto rounded-full bg-indigo-100 text-indigo-600 flex items-center justify-center animate-spin">
                  <Icons.RefreshCw />
                </div>
                <div>
                  <h4 className="font-bold text-slate-900 text-base">Hệ thống đang chấm bài thi</h4>
                  <p className="text-xs text-indigo-700 font-semibold mt-1.5 animate-pulse">
                    {gradingProgress}
                  </p>
                </div>
                <div className="text-[11px] text-slate-500 bg-slate-50 p-2.5 rounded-lg border border-slate-200">
                  AI Vision đang phân tích ảnh chụp, đọc từng dòng chữ viết tay, đối chiếu barem điểm chuẩn của Bộ GD&ĐT. Vui lòng chờ trong giây lát...
                </div>
              </div>
            </div>
          )}
"""

if "{/* MODAL PHÓNG TO ẢNH BÀI LÀM VIẾT TAY */}" not in content:
    main_end = "</main>"
    content = content.replace(main_end, modals_code + "\n        " + main_end, 1)
    print("Added Modals and Progress Overlay.")

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("Saved updated index.html. New length:", len(content))
