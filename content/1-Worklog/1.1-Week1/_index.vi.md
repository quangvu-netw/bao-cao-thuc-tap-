---
title: "Worklog Tuần 1"
date: 2026-04-20
weight: 1
chapter: false
pre: " <b> 1.1. </b> "
---

### Mục tiêu tuần 1:

* Kết nối, làm quen với các thành viên trong First Cloud Journey.
* Hiểu dịch vụ AWS cơ bản, cách dùng console & CLI.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc                                                                                                                                                                                             | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu                         |
|:-----|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|:-------------------|:------------------------------------------|
| 2   | - Làm quen với các thành viên FCJ <br> - Đọc và lưu ý các nội quy, quy định tại đơn vị thực tập                                                                                     | 20/04/2026 | 20/04/2026 |                                           |
| 3   | - Tìm hiểu AWS và các loại dịch vụ <br>&emsp; + Compute <br>&emsp; + Storage <br>&emsp; + Networking <br>&emsp; + Database <br>&emsp; + ... <br>                                                 | 21/04/2026 | 21/04/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 4   | - Tạo AWS Free Tier account <br> - Tìm hiểu AWS Console & AWS CLI <br> - **Thực hành:** <br>&emsp; + Tạo AWS account <br>&emsp; + Cài AWS CLI & cấu hình <br> &emsp; + Cách sử dụng AWS CLI | 22/04/2026 | 22/04/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 5   | - Tìm hiểu EC2 cơ bản: <br>&emsp; + Instance types <br>&emsp; + AMI <br>&emsp; + EBS <br>&emsp; + ... <br> - Các cách remote SSH vào EC2 <br> - Tìm hiểu Elastic IP   <br>                     | 23/04/2026 | 23/04/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 6   | - **Thực hành:** <br>&emsp; + Tạo EC2 instance <br>&emsp; + Kết nối SSH <br>&emsp; + Gắn EBS volume                                                                                               | 24/04/2026 | 24/04/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 7 - CN | - **Thực hành nâng cao:** <br>&emsp; + Khởi tạo lại EC2 instance và cấu hình Security Group <br>&emsp; + Kết nối SSH và cài đặt Web Server (Apache/Nginx) <br>&emsp; + Triển khai web đơn giản và truy cập qua Public IP <br>&emsp; + Tìm hiểu và thử nghiệm AWS S3 (tạo bucket, upload file) <br>&emsp; + Thực hành thêm các lệnh AWS CLI | 25/04/2026 | 26/04/2026 | <https://cloudjourney.awsstudygroup.com/> |
### Kết quả đạt được tuần 1:

* Hiểu AWS là gì và nắm được các nhóm dịch vụ cơ bản:
  * Compute (EC2)
  * Storage (S3, EBS)
  * Networking (VPC)
  * Database (RDS, DynamoDB)

---

* Quản trị AWS (Console & CLI): Thành thạo giao diện Web và AWS CLI (cấu hình Access Key, quản lý vùng, kiểm tra trạng thái tài nguyên). 

---

* Hạ tầng & Web Server (EC2 & Linux): Khởi tạo EC2 (Amazon Linux), cấu hình Security Group, kết nối SSH và triển khai thành công Web Server (Apache/Nginx) qua Public IP. 
 
---

* Lưu trữ dữ liệu (EBS & S3): Tạo và mount EBS Volume vào hệ thống file Linux; khởi tạo và upload dữ liệu lên S3 Bucket.