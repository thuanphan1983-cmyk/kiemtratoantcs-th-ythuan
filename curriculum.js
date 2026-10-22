// ==============================================================================
// DANH MỤC CHƯƠNG TRÌNH SGK TOÁN THCS KẾT NỐI TRI THỨC VỚI CUỘC SỐNG (LỚP 6, 7, 8, 9)
// Bao gồm đầy đủ Tập 1 và Tập 2 theo chuẩn chương trình GDPT 2018 của Bộ GD&ĐT
// ==============================================================================

const CURRICULUM_KNTT = {
  "6": {
    name: "Toán 6 - Kết nối tri thức",
    chapters: [
      {
        id: "c1_6",
        title: "Chương I: Tập hợp các số tự nhiên",
        lessons: [
          "Bài 1: Tập hợp",
          "Bài 2: Cách ghi số tự nhiên",
          "Bài 3: Thứ tự trong tập hợp các số tự nhiên",
          "Bài 4: Phép cộng và phép trừ số tự nhiên",
          "Bài 5: Phép nhân và phép chia số tự nhiên",
          "Bài 6: Lũy thừa với số mũ tự nhiên",
          "Bài 7: Thứ tự thực hiện các phép tính"
        ]
      },
      {
        id: "c2_6",
        title: "Chương II: Tính chia hết trong tập hợp các số tự nhiên",
        lessons: [
          "Bài 8: Quan hệ chia hết và tính chất",
          "Bài 9: Dấu hiệu chia hết",
          "Bài 10: Số nguyên tố",
          "Bài 11: Ước chung. Ước chung lớn nhất",
          "Bài 12: Bội chung. Bội chung nhỏ nhất"
        ]
      },
      {
        id: "c3_6",
        title: "Chương III: Số nguyên",
        lessons: [
          "Bài 13: Tập hợp các số nguyên",
          "Bài 14: Phép cộng và phép trừ số nguyên",
          "Bài 15: Quy tắc dấu ngoặc",
          "Bài 16: Phép nhân số nguyên",
          "Bài 17: Phép chia hết. Ước và bội của một số nguyên"
        ]
      },
      {
        id: "c4_6",
        title: "Chương IV: Một số hình phẳng trong thực tiễn",
        lessons: [
          "Bài 18: Hình tam giác đều. Hình vuông. Hình lục giác đều",
          "Bài 19: Hình chữ nhật. Hình thoi",
          "Bài 20: Hình bình hành. Hình thang cân"
        ]
      },
      {
        id: "c5_6",
        title: "Chương V: Tính đối xứng của hình phẳng trong tự nhiên",
        lessons: [
          "Bài 21: Hình có trục đối xứng",
          "Bài 22: Hình có tâm đối xứng"
        ]
      },
      {
        id: "c6_6",
        title: "Chương VI: Phân số",
        lessons: [
          "Bài 23: Mở rộng phân số. Phân số bằng nhau",
          "Bài 24: So sánh phân số. Hỗn số dương",
          "Bài 25: Phép cộng và phép trừ phân số",
          "Bài 26: Phép nhân và phép chia phân số",
          "Bài 27: Hai bài toán về phân số"
        ]
      },
      {
        id: "c7_6",
        title: "Chương VII: Số thập phân",
        lessons: [
          "Bài 28: Số thập phân",
          "Bài 29: Tính toán với số thập phân",
          "Bài 30: Làm tròn và ước lượng",
          "Bài 31: Một số bài toán về tỉ số và tỉ số phần trăm"
        ]
      },
      {
        id: "c8_6",
        title: "Chương VIII: Những hình hình học cơ bản",
        lessons: [
          "Bài 32: Điểm và đường thẳng",
          "Bài 33: Điểm nằm giữa hai điểm. Tia",
          "Bài 34: Đoạn thẳng. Độ dài đoạn thẳng",
          "Bài 35: Trung điểm của đoạn thẳng",
          "Bài 36: Góc",
          "Bài 37: Số đo góc"
        ]
      },
      {
        id: "c9_6",
        title: "Chương IX: Dữ liệu và xác suất thực nghiệm",
        lessons: [
          "Bài 38: Dữ liệu và thu thập dữ liệu",
          "Bài 39: Bảng thống kê và biểu đồ tranh",
          "Bài 40: Biểu đồ cột",
          "Bài 41: Biểu đồ cột kép",
          "Bài 42: Kết quả có thể và sự kiện trong trò chơi, thí nghiệm",
          "Bài 43: Xác suất thực nghiệm"
        ]
      }
    ]
  },
  "7": {
    name: "Toán 7 - Kết nối tri thức",
    chapters: [
      {
        id: "c1_7",
        title: "Chương I: Số hữu tỉ",
        lessons: [
          "Bài 1: Tập hợp các số hữu tỉ",
          "Bài 2: Cộng, trừ, nhân, chia số hữu tỉ",
          "Bài 3: Lũy thừa với số mũ tự nhiên của một số hữu tỉ",
          "Bài 4: Thứ tự thực hiện các phép tính. Quy tắc chuyển vế"
        ]
      },
      {
        id: "c2_7",
        title: "Chương II: Số thực",
        lessons: [
          "Bài 5: Làm quen với số thập phân vô hạn tuần hoàn",
          "Bài 6: Số vô tỉ. Căn bậc hai số học",
          "Bài 7: Tập hợp các số thực"
        ]
      },
      {
        id: "c3_7",
        title: "Chương III: Góc và đường thẳng song song",
        lessons: [
          "Bài 8: Góc ở vị trí đặc biệt. Tia phân giác của một góc",
          "Bài 9: Hai đường thẳng song song và dấu hiệu nhận biết",
          "Bài 10: Tiên đề Euclid. Tính chất của hai đường thẳng song song",
          "Bài 11: Định lí và chứng minh định lí"
        ]
      },
      {
        id: "c4_7",
        title: "Chương IV: Tam giác bằng nhau",
        lessons: [
          "Bài 12: Tổng các góc trong một tam giác",
          "Bài 13: Hai tam giác bằng nhau. Trường hợp bằng nhau thứ nhất của tam giác (c.c.c)",
          "Bài 14: Trường hợp bằng nhau thứ hai và thứ ba của tam giác (c.g.c, g.c.g)",
          "Bài 15: Các trường hợp bằng nhau của tam giác vuông",
          "Bài 16: Tam giác cân. Đường trung trực của đoạn thẳng"
        ]
      },
      {
        id: "c5_7",
        title: "Chương V: Thu thập và biểu diễn dữ liệu",
        lessons: [
          "Bài 17: Thu thập và phân loại dữ liệu",
          "Bài 18: Biểu đồ hình quạt tròn",
          "Bài 19: Biểu đồ đoạn thẳng"
        ]
      },
      {
        id: "c6_7",
        title: "Chương VI: Tỉ lệ thức và đại lượng tỉ lệ",
        lessons: [
          "Bài 20: Tỉ lệ thức",
          "Bài 21: Tính chất của dãy tỉ số bằng nhau",
          "Bài 22: Đại lượng tỉ lệ thuận",
          "Bài 23: Đại lượng tỉ lệ nghịch"
        ]
      },
      {
        id: "c7_7",
        title: "Chương VII: Biểu thức đại số và đa thức một biến",
        lessons: [
          "Bài 24: Biểu thức đại số",
          "Bài 25: Đa thức một biến",
          "Bài 26: Phép cộng và phép trừ đa thức một biến",
          "Bài 27: Phép nhân đa thức một biến",
          "Bài 28: Phép chia đa thức một biến"
        ]
      },
      {
        id: "c8_7",
        title: "Chương VIII: Làm quen với biến cố và xác suất của biến cố",
        lessons: [
          "Bài 29: Làm quen với biến cố",
          "Bài 30: Làm quen với xác suất của biến cố"
        ]
      },
      {
        id: "c9_7",
        title: "Chương IX: Quan hệ giữa các yếu tố trong một tam giác",
        lessons: [
          "Bài 31: Quan hệ giữa góc và cạnh đối diện trong một tam giác",
          "Bài 32: Quan hệ giữa đường vuông góc và đường xiên",
          "Bài 33: Quan hệ giữa ba cạnh của một tam giác",
          "Bài 34: Sự đồng quy của ba đường trung tuyến, ba đường phân giác trong một tam giác",
          "Bài 35: Sự đồng quy của ba đường trung trực, ba đường cao trong một tam giác"
        ]
      },
      {
        id: "c10_7",
        title: "Chương X: Một số hình khối trong thực tiễn",
        lessons: [
          "Bài 36: Hình hộp chữ nhật và hình lập phương",
          "Bài 37: Hình lăng trụ đứng tam giác và hình lăng trụ đứng tứ giác"
        ]
      }
    ]
  },
  "8": {
    name: "Toán 8 - Kết nối tri thức",
    chapters: [
      {
        id: "c1_8",
        title: "Chương I: Đa thức",
        lessons: [
          "Bài 1: Đơn thức",
          "Bài 2: Đa thức",
          "Bài 3: Phép cộng và phép trừ đa thức",
          "Bài 4: Phép nhân đa thức",
          "Bài 5: Phép chia đa thức cho đơn thức"
        ]
      },
      {
        id: "c2_8",
        title: "Chương II: Hằng đẳng thức đáng nhớ và ứng dụng",
        lessons: [
          "Bài 6: Hiệu hai bình phương. Bình phương của một tổng hay một hiệu",
          "Bài 7: Lập phương của một tổng. Lập phương của một hiệu",
          "Bài 8: Tổng và hiệu hai lập phương",
          "Bài 9: Phân tích đa thức thành nhân tử"
        ]
      },
      {
        id: "c3_8",
        title: "Chương III: Tứ giác",
        lessons: [
          "Bài 10: Tứ giác",
          "Bài 11: Hình thang cân",
          "Bài 12: Hình bình hành",
          "Bài 13: Hình chữ nhật",
          "Bài 14: Hình thoi và hình vuông"
        ]
      },
      {
        id: "c4_8",
        title: "Chương IV: Định lí Thalès",
        lessons: [
          "Bài 15: Định lí Thalès trong tam giác",
          "Bài 16: Đường trung bình của tam giác",
          "Bài 17: Tính chất đường phân giác của tam giác"
        ]
      },
      {
        id: "c5_8",
        title: "Chương V: Dữ liệu và biểu đồ",
        lessons: [
          "Bài 18: Thu thập và phân loại dữ liệu",
          "Bài 19: Biểu diễn dữ liệu bằng bảng, biểu đồ",
          "Bài 20: Phân tích số liệu thống kê dựa vào biểu đồ"
        ]
      },
      {
        id: "c6_8",
        title: "Chương VI: Phân thức đại số",
        lessons: [
          "Bài 21: Phân thức đại số",
          "Bài 22: Tính chất cơ bản của phân thức đại số",
          "Bài 23: Phép cộng và phép trừ phân thức đại số",
          "Bài 24: Phép nhân và phép chia phân thức đại số"
        ]
      },
      {
        id: "c7_8",
        title: "Chương VII: Phương trình bậc nhất và hàm số bậc nhất",
        lessons: [
          "Bài 25: Phương trình bậc nhất một ẩn",
          "Bài 26: Giải bài toán bằng cách lập phương trình",
          "Bài 27: Khái niệm hàm số và đồ thị của hàm số",
          "Bài 28: Hàm số bậc nhất $y = ax + b$ ($a \\neq 0$)",
          "Bài 29: Hệ số góc của đường thẳng"
        ]
      },
      {
        id: "c8_8",
        title: "Chương VIII: Mở đầu về tính xác suất của biến cố",
        lessons: [
          "Bài 30: Kết quả có thể và kết quả thuận lợi",
          "Bài 31: Cách tính xác suất của biến cố bằng tỉ số",
          "Bài 32: Mối liên hệ giữa xác suất thực nghiệm với xác suất ứng dụng"
        ]
      },
      {
        id: "c9_8",
        title: "Chương IX: Tam giác đồng dạng",
        lessons: [
          "Bài 33: Hai tam giác đồng dạng",
          "Bài 34: Ba trường hợp đồng dạng của hai tam giác",
          "Bài 35: Định lí Pythagore và ứng dụng",
          "Bài 36: Các trường hợp đồng dạng của hai tam giác vuông",
          "Bài 37: Hình đồng dạng"
        ]
      },
      {
        id: "c10_8",
        title: "Chương X: Một số hình khối trong thực tiễn",
        lessons: [
          "Bài 38: Hình chóp tam giác đều",
          "Bài 39: Hình chóp tứ giác đều"
        ]
      }
    ]
  },
  "9": {
    name: "Toán 9 - Kết nối tri thức",
    chapters: [
      {
        id: "c1_9",
        title: "Chương I: Phương trình và hệ hai phương trình bậc nhất hai ẩn",
        lessons: [
          "Bài 1: Khái niệm phương trình và hệ hai phương trình bậc nhất hai ẩn",
          "Bài 2: Giải hệ hai phương trình bậc nhất hai ẩn",
          "Bài 3: Giải bài toán bằng cách lập hệ phương trình"
        ]
      },
      {
        id: "c2_9",
        title: "Chương II: Phương trình và bất phương trình bậc nhất một ẩn",
        lessons: [
          "Bài 4: Phương trình quy về phương trình bậc nhất một ẩn",
          "Bài 5: Bất đẳng thức và tính chất",
          "Bài 6: Bất phương trình bậc nhất một ẩn"
        ]
      },
      {
        id: "c3_9",
        title: "Chương III: Căn bậc hai và căn bậc ba",
        lessons: [
          "Bài 7: Căn bậc hai và căn thức bậc hai",
          "Bài 8: Khai căn bậc hai với phép nhân và phép chia",
          "Bài 9: Biến đổi đơn giản và rút gọn biểu thức chứa căn thức bậc hai",
          "Bài 10: Căn bậc ba và căn thức bậc ba"
        ]
      },
      {
        id: "c4_9",
        title: "Chương IV: Hệ thức lượng trong tam giác vuông",
        lessons: [
          "Bài 11: Tỉ số lượng giác của góc nhọn",
          "Bài 12: Một số hệ thức giữa cạnh, góc trong tam giác vuông và ứng dụng"
        ]
      },
      {
        id: "c5_9",
        title: "Chương V: Đường tròn",
        lessons: [
          "Bài 13: Mở đầu về đường tròn",
          "Bài 14: Cung và dây của một đường tròn",
          "Bài 15: Độ dài của cung tròn. Diện tích hình quạt tròn và hình vành khuyên",
          "Bài 16: Vị trí tương đối của đường thẳng và đường tròn",
          "Bài 17: Vị trí tương đối của hai đường tròn"
        ]
      },
      {
        id: "c6_9",
        title: "Chương VI: Hàm số $y = ax^2$ ($a \\neq 0$). Phương trình bậc hai một ẩn",
        lessons: [
          "Bài 18: Hàm số $y = ax^2$ ($a \\neq 0$)",
          "Bài 19: Phương trình bậc hai một ẩn",
          "Bài 20: Định lí Viète và ứng dụng",
          "Bài 21: Giải bài toán bằng cách lập phương trình"
        ]
      },
      {
        id: "c7_9",
        title: "Chương VII: Tần số và tần số tương đối",
        lessons: [
          "Bài 22: Bảng tần số và biểu đồ tần số",
          "Bài 23: Bảng tần số tương đối và biểu đồ tần số tương đối",
          "Bài 24: Bảng tần số ghép nhóm và biểu đồ"
        ]
      },
      {
        id: "c8_9",
        title: "Chương VIII: Xác suất của biến cố trong một số mô hình xác suất đơn giản",
        lessons: [
          "Bài 25: Phép thử ngẫu nhiên và không gian mẫu",
          "Bài 26: Xác suất của biến cố liên quan đến phép thử"
        ]
      },
      {
        id: "c9_9",
        title: "Chương IX: Đường tròn ngoại tiếp và đường tròn nội tiếp",
        lessons: [
          "Bài 27: Góc nội tiếp",
          "Bài 28: Đường tròn ngoại tiếp và đường tròn nội tiếp của một tam giác",
          "Bài 29: Tứ giác nội tiếp",
          "Bài 30: Đa giác đều"
        ]
      },
      {
        id: "c10_9",
        title: "Chương X: Một số hình khối trong thực tiễn",
        lessons: [
          "Bài 31: Hình trụ và hình nón",
          "Bài 32: Hình cầu"
        ]
      }
    ]
  }
};

// Đảm bảo tương thích cả Node.js (module.exports) và Trình duyệt (window.CURRICULUM_KNTT)
if (typeof module !== "undefined" && module.exports) {
  module.exports = { CURRICULUM_KNTT };
}
if (typeof window !== "undefined") {
  window.CURRICULUM_KNTT = CURRICULUM_KNTT;
}
