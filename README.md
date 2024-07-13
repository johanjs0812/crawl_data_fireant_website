Phần mềm trích xuất dữ liệu thông qua trang web FireAnt
Bản cập nhật ngày 12/07/2024

Chức năng hiện có:

1. Trích xuất dữ liệu 4 trang:

- Cân đối kế toán
- Kết quả kinh doanh
- LCTT trực tiếp 
- LCTT gián tiếp

2. Chuyển đổi sang định dạng file Json.

Có thể tùy ý số lượng cổ phiếu muốn trích xuất thông tin thông qua file setting.py trong thư mục config. Giới hạn trích xuất dữ liệu được đặt là từ đây trở về đến quý 1 2014 tương đương 10 năm. Có thể chỉnh sửa giới hạn tùy ý, tuy nhiên tác giả chưa thử nghiệm các trường hợp lâu hơn, mọi trục trặc miễn trừ trách nhiệm.

Khởi chạy:

- Download dự án về thư mục và mở trên VSCODE
- Trên TERMINAL dự án gõ: 
+ python -m venv myenv (để tạo máy ảo)
+ myenv\Scripts\activate (kích họat máy ảo đối với Windows)
+ source myenv/bin/activate (kích họat máy ảo đối với MacOS và Linux)
+ pip install -r requirements.txt (cài đặt các thư viện cần thiết cho dự án)
+ python main.py (để khởi chạy dự án)

YÊU CẦU: Python 3.9.0 trở lên. Mọi phiên bản khác có thể không vấn đề nếu bạn am hiểu Python có thể lựa chọn các phiên bản khác nếu muốn. Tuy nhiên Python 3.9.0 là phiên bản được sử dụng để lập trình lên phần mềm này vì vậy mọi trục trặc do sử dụng những phiên bản khác miễn trừ trách nhiệm. Các phiên bản thư viện hỗ trợ được ghi trong tệp requirements.txt tương tự.

Phần mềm được xây dựng nhằm mang mục đích nghiên cứu học tập không vì bất cứ mục đích thương mại nào khác.

- Pham Tan