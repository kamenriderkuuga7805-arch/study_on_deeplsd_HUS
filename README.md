# study_on_deeplsd_HUS
Đề tài tiểu luận: "Nghiên cứu và ứng dụng phương pháp DeepLSD trong phát hiện đoạn thẳng" dành cho học phần "Đồ án Kỹ thuật điện tử và Tin học" thầy TS. Phạm Văn Thành, TS. Nguyễn Tiến Cường được hướng dẫn bởi CN. Vi Anh Quân

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1nmM5JDjfC568SmrWyYc-rFnM_b18MsqN#scrollTo=pCDBt4IK1aa2)

## 📌 Giới thiệu
Dự án tập trung nghiên cứu, cài đặt thử nghiệm và ứng dụng mạng nơ-ron sâu **DeepLSD (Deep Line Segment Detector)** để tự động phát hiện các đoạn thẳng từ ảnh kỹ thuật số trên môi trường Python.  
Bài toán tiếp cận theo hướng tham khảo và cài lại để kiểm chứng từ các mô hình đã được huấn luyện sẵn để trích xuất các đoạn thẳng với độ chính xác cao ở cấp độ pixel dưới dạng các ma trận tọa độ dòng.

Mô hình ứng dụng kết hợp:
- **DeepLSD**: Tận dụng cả đặc trưng vùng và đặc trưng biên (Gradient) để tối ưu hóa việc nhận diện đoạn thẳng một cách liền mạch.
- **Pre-trained Weights**: Sử dụng các bộ trọng số đã tối ưu sẵn từ nhóm tác giả (`deeplsd_md` và `deeplsd_wireframe`) phục vụ cho việc suy luận nhanh.

---

### Mục tiêu

- Cấu hình môi trường, tích hợp mã nguồn DeepLSD và cài đặt các phụ thuộc (Dependencies).
- Tải và nạp các bộ trọng số pre-trained (`.tar`) vào kiến trúc mô hình trên GPU.
- Tiền xử lý ảnh đầu vào thành định dạng ảnh xám (Grayscale) và chuẩn hóa tensor.
- Thực hiện suy luận để trích xuất tọa độ các đoạn thẳng và số lượng đường tìm thấy.
- Trực quan hóa kết quả: Vẽ đè các đoạn thẳng phát hiện được lên ảnh RGB gốc bằng Matplotlib để đánh giá định tính.

---

### Thư viện và công cụ sử dụng

| Thư viện | Vai trò |
|---|---|
| **PyTorch** | Khởi tạo cấu trúc mạng, load trọng số pre-trained và chạy inference trên GPU |
| **DeepLSD (CVG Group)** | Framework mã nguồn mở chính cho bài toán nhận diện đoạn thẳng |
| **pytlsd** | Thư viện hỗ trợ thuật toán LSD truyền thống đi kèm |
| **OpenCV** | Đọc ảnh, chuyển đổi hệ màu và xử lý ma trận điểm ảnh |
| **NumPy** | Xử lý dữ liệu cấu trúc tọa độ mảng 2D/3D |
| **Matplotlib** | Trực quan hóa ảnh gốc và vẽ đồ thị các đường thẳng phát hiện được |

---

### Những khó khăn gặp phải

Trong quá trình thực hiện bài toán thực nghiệm, dự án đối mặt với một số vấn đề:
- Môi trường Google Colab thường xuyên bị reset hoặc ngắt kết nối giữa các phiên (Session), dẫn đến việc mất cấu hình biến môi trường `sys.path` và phải cài đặt lại thư viện từ đầu.
- Việc đồng bộ và quản lý đường dẫn thư mục con (`/content/DeepLSD/deeplsd`) dễ gây ra lỗi `ModuleNotFoundError` nếu không trích xuất PATH chính xác trước khi import.
- Biến đổi hệ tọa độ của ma trận kết quả đầu ra khi hiển thị ngược lại lên nền thư viện đồ họa Matplotlib dễ bị lệch nếu không đảo cấu trúc index `[x, y]`.

---

### Hướng phát triển

- Ứng dụng kết quả nhận diện đoạn thẳng của DeepLSD vào bài toán **Vanishing Point Detection** (Tìm điểm tụ) hoặc ước lượng cấu trúc phòng 3D (Wireframe parsing).
- Thử nghiệm trên các luồng video trực tuyến (Real-time Video Inference).
- Tích hợp mô hình vào một ứng dụng Web Demo trực quan (Gradio / Streamlit).

---

## 🚀 Hướng dẫn cài đặt và chạy dự án
Do đây là dự án được chạy từ weights có sẵn của tác giả gốc nên cần thực hiện 1 vài bước cài đặt trước khi chạy thành công:
- Cài đặt mã nguồn và môi trường:

%cd /content

!git clone --recurse-submodules https://github.com/cvg/DeepLSD.git

%cd DeepLSD

!bash quickstart_install.sh

!pip install pytlsd

- Cài weights sẵn:

!mkdir weights

!wget https://cvg-data.inf.ethz.ch/DeepLSD/deeplsd_wireframe.tar -O weights/deeplsd_wireframe.tar

!wget https://cvg-data.inf.ethz.ch/DeepLSD/deeplsd_md.tar -O weights/deeplsd_md.tar

!pip install pytlsd

- Clone repository:

git clone https://github.com/kamenriderkuuga7805-arch/study_on_deeplsd_HUS.git

cd study_on_deeplsd_HUS

Có thể tự tải ảnh từ thiết bị cá nhân hoặc dùng ảnh trong folder Test_Pictures đã được upload bên trên
