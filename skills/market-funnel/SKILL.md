# Phân tích & Tối ưu hóa Phễu Bán hàng (Sales Funnel Analysis)

Bạn là công cụ phân tích phễu cho câu lệnh `/market funnel <url>`. Bạn sẽ lập sơ đồ toàn bộ hành trình chuyển đổi từ lượt truy cập đầu tiên đến khi mua hàng, xác định các điểm rơi rớt khách hàng (drop-off points), đo lường mức độ ma sát (friction), và đưa ra các khuyến nghị tối ưu hóa cụ thể kèm theo ước tính tác động doanh thu. Mỗi đề xuất cải tiến đều được sắp xếp thứ tự ưu tiên dựa trên mức độ tăng trưởng kỳ vọng và nỗ lực triển khai thực tế.

## Khi Kỹ năng này được Gọi

Người dùng chạy lệnh `/market funnel <url>`. Quét trang web mục tiêu và theo dấu từng bước chân một khách truy cập thực hiện từ lúc đặt chân đến trang cho tới khi chuyển đổi thành công. Phân tích từng bước về độ ma sát, tính rõ ràng và mức độ hiệu quả. Xuất báo cáo hoàn chỉnh vào file `FUNNEL-ANALYSIS.md`.

---

## Giai đoạn 1: Tìm hiểu và Lập sơ đồ Phễu (Funnel)

### 1.1 Xác định loại Phễu (Funnel Type)

Nhận diện loại phễu trang web đang áp dụng:

| Loại phễu | Mô hình kinh doanh | Các bước điển hình | Chỉ số KPI chính |
|-------------|---------------|---------------|------------|
| **Lead Gen** | Dịch vụ, agency, B2B | Landing page -> Điền form -> Cảm ơn -> Nuôi dưỡng -> Cuộc hẹn sales | Tỷ lệ chốt hợp đồng (Lead-to-close) |
| **SaaS Trial** | Sản phẩm phần mềm | Trang chủ -> Bảng giá -> Đăng ký -> Hướng dẫn -> Nâng cấp gói trả phí | Tỷ lệ chuyển đổi dùng thử (Trial-to-paid) |
| **SaaS Demo** | Phần mềm B2B doanh nghiệp | Trang chủ -> Các tính năng -> Yêu cầu demo -> Gọi điện sales -> Chốt đơn | Tỷ lệ chuyển đổi từ xem demo |
| **E-commerce** | Cửa hàng bán lẻ trực tuyến | Trang sản phẩm -> Giỏ hàng -> Thanh toán -> Bán thêm (upsell) -> Cảm ơn | Tỷ lệ mua hàng từ giỏ hàng |
| **Webinar** | Khóa học, đào tạo, SaaS | Đăng ký nhận link -> Xác nhận -> Nhắc lịch -> Xem live -> Ưu đãi -> Thanh toán | Tỷ lệ mua hàng từ webinar |
| **Application** | Dịch vụ cao cấp, chương trình VIP | Trang thông tin -> Form nộp đơn -> Duyệt hồ sơ -> Phỏng vấn -> Nhập học/Hợp tác | Tỷ lệ nộp đơn thành công |
| **Community** | Gói thành viên, cộng đồng | Landing page -> Dùng thử/Xem trước -> Tương tác -> Trả phí thành viên | Tỷ lệ gia hạn trả phí |
| **Content** | Trang báo chí, truyền thông | Bài viết blog -> Đăng ký nhận tin -> Nuôi dưỡng -> Đọc premium -> Đăng ký trả phí | Tỷ lệ người đọc đăng ký |

### 1.2 Lập sơ đồ chi tiết từng bước phễu

Đối với mỗi trang trong phễu, hãy ghi chép thông tin:

```
BƯỚC [#]: [Tên trang]
  URL: [url]
  Loại trang: [landing/product/pricing/cart/checkout/form/thank-you]
  Hành động chính: [người dùng nên làm gì trên trang này]
  Bước tiếp theo: [người dùng sẽ đi đâu tiếp theo]
  Điểm thoát (Exit Points): [nơi người dùng có thể rời bỏ trang thay vì đi tiếp]
  Yếu tố ma sát (Friction): [bất kỳ điều gì gây cản trở hoặc làm bối rối]
  Tín hiệu uy tín (Trust): [bất kỳ yếu tố nào củng cố niềm tin]
  Thời gian tải trang: [ước tính dựa trên độ phức tạp của trang]
```

### 1.3 Bản đồ Phễu Trực quan (Visual Funnel Map)

Tạo một bản đồ phễu bằng ký tự ASCII thể hiện luồng đi của khách hàng:

```
BẢN ĐỒ HÀNH TRÌNH KHÁCH HÀNG
===========================

Nguồn Traffic
  |
  v
[Trang chủ] ─── 100% lượng truy cập
  |
  v
[Trang bảng giá] ─── ~30% tỷ lệ click đi tiếp
  |
  v
[Form đăng ký] ─── ~15% tiếp cận form đăng ký
  |
  v
[Onboarding] ─── ~10% hoàn tất đăng ký tài khoản
  |
  v
[Tương tác sử dụng] ─── ~6% đạt mức kích hoạt tính năng
  |
  v
[Nâng cấp trả phí] ─── ~2% chuyển đổi sang gói trả phí

Tổng quan: 2% tỷ lệ chuyển đổi từ visitor sang gói trả phí
```

Điều chỉnh sơ đồ trên để khớp chính xác với cấu trúc phễu thực tế phát hiện được trên website.

---

## Giai đoạn 2: Phân tích chi tiết từng trang

### 2.1 Khung Phân tích

Đối với mỗi trang trong phễu, hãy chấm điểm theo các khía cạnh (thang điểm 0-10):

| Khía cạnh đánh giá | Điểm số (0-10) | Tiêu chí đánh giá |
|-----------|-------------|------------------|
| **Clarity** (Tính rõ ràng) | 0-10 | Mục đích của trang này có dễ nhận biết ngay lập tức không? |
| **Continuity** (Tính liên tục) | 0-10 | Trang này có tiếp nối logic từ bước trước đó không? |
| **Motivation** (Động lực) | 0-10 | Trang này có trao đủ động lực để người dùng đi tiếp không? |
| **Friction** (Ma sát) | 0-10 | Việc thực hiện hành động mong muốn dễ dàng ra sao? (10 = mượt mà nhất) |
| **Trust** (Độ tin cậy) | 0-10 | Có đủ các tín hiệu uy tín cần thiết cho giai đoạn này không? |

**Điểm số của Trang = Trung bình cộng của cả 5 khía cạnh (thang điểm 0-10)**

### 2.2 Các điểm rơi rớt khách hàng (Drop-Off) phổ biến và cách sửa

**Từ Trang chủ đi tới bước tiếp theo:**
| Nguyên nhân rơi rớt | Dấu hiệu nhận biết | Giải pháp xử lý |
|----------------|-----------------|-----|
| Value Proposition không rõ ràng | Headline mơ hồ, thiếu cụ thể | Viết lại Headline hướng trực tiếp vào kết quả |
| Không có CTA rõ ràng | Có quá nhiều nút CTA đồng hạng, CTA nằm dưới nếp gấp màn hình | Đặt duy nhất một CTA chính trên nếp gấp đầu tiên |
| Tốc độ tải trang chậm | Hình ảnh quá nặng, nhiều script chạy ngầm | Tối ưu hóa dung lượng ảnh, trì hoãn JS không quan trọng |
| Trải nghiệm di động kém | Chữ quá nhỏ, các nút đặt quá sát nhau khó bấm | Thiết kế lại giao diện di động theo chuẩn mobile-first |

**Trang bảng giá (Pricing Page):**
| Nguyên nhân rơi rớt | Dấu hiệu nhận biết | Giải pháp xử lý |
|----------------|-----------------|-----|
| Sốc giá tiền | Đưa giá trực tiếp khi chưa xây dựng giá trị | Đưa khung giá trị (value) lên trước phần bảng giá |
| Có quá nhiều lựa chọn | Có từ 4 gói trở lên, tính năng liệt kê quá tải | Rút gọn còn tối đa 3 gói, làm nổi bật gói khuyên dùng |
| Phí ẩn phát sinh | Các khoản phí phụ chỉ được thấy ở bước sau | Minh bạch thông tin chi phí ngay từ đầu |
| Thiếu Social Proof | Không có testimonial cạnh phần bảng giá | Bổ sung ý kiến khách hàng hoặc con số uy tín cạnh các gói giá |
| Thiếu phần câu hỏi FAQ | Các thắc mắc thường gặp chưa có lời giải đáp | Bổ sung FAQ giải đáp 5 điểm ngần ngại lớn nhất về giá |

**Trang Đăng ký/Tạo tài khoản:**
| Nguyên nhân rơi rớt | Dấu hiệu nhận biết | Giải pháp xử lý |
|----------------|-----------------|-----|
| Form quá nhiều trường thông tin | Bắt điền trên 5 trường bắt buộc | Giảm xuống còn tối đa 3 trường (tên, email, pass) |
| Bắt tạo tài khoản quá sớm | Bắt đăng ký mới cho xem nội dung | Cho phép trải nghiệm thử trước khi bắt tạo tài khoản |
| Thiếu thanh tiến trình | Form nhiều bước nhưng không có chỉ dẫn | Thêm bộ đếm bước trực quan: "Bước 1 trên 3" |
| Thiếu đăng nhập nhanh | Chỉ cho đăng ký thủ công bằng email/pass | Bổ sung đăng nhập nhanh qua Google/GitHub/SSO |
| Thiếu tín hiệu uy tín | Không có cam kết bảo mật, thiếu chứng chỉ | Thêm dòng cam kết bảo mật thông tin, biểu tượng an toàn |

**Trang Thanh toán/Mua hàng:**
| Nguyên nhân rơi rớt | Dấu hiệu nhận biết | Giải pháp xử lý |
|----------------|-----------------|-----|
| Bất ngờ phí vận chuyển | Phí ship chỉ xuất hiện ở bước thanh toán cuối | Công bố phí ship sớm hoặc áp dụng chính sách miễn phí vận chuyển |
| Bắt tạo tài khoản bắt buộc | Không cho thanh toán nhanh | Bổ sung tùy chọn mua hàng nhanh không cần tạo tài khoản (guest checkout) |
| Hạn chế phương thức thanh toán | Chỉ chấp nhận thẻ tín dụng | Bổ sung PayPal, Apple Pay, Google Pay, chuyển khoản |
| Thiếu tính khẩn cấp | Không có động lực để mua ngay hôm nay | Thêm số lượng giới hạn, đồng hồ đếm ngược, quà tặng đi kèm |
| Thiếu cam kết bảo hành | Chính sách đổi trả không rõ ràng | Hiển thị chính sách cam kết hoàn tiền nổi bật cạnh nút mua |

### 2.3 Đánh giá hiệu quả của Lead Magnet

Nếu phễu bán hàng có sử dụng Lead Magnet, hãy đánh giá theo các tiêu chí (0-10):

| Tiêu chí | Điểm số (0-10) | Nội dung đánh giá |
|----------|-------------|------------|
| **Relevance** (Mức độ liên quan) | 0-10 | Có nhắm trúng nỗi đau (pain) lớn nhất của đối tượng mục tiêu không? |
| **Specificity** (Tính cụ thể) | 0-10 | Định dạng đầu ra có rõ ràng không (tránh viết chung chung "cuốn hướng dẫn")? |
| **Perceived Value** (Giá trị cảm nhận) | 0-10 | Người dùng có sẵn sàng trả $20+ để có được tài liệu này không? |
| **Quick Win** (Giá trị tức thì) | 0-10 | Người dùng có nhận được giá trị thực tế trong vòng 10 phút đầu đọc không? |
| **Product Alignment** (Đồng bộ sản phẩm) | 0-10 | Có dẫn dắt người dùng mong muốn sở hữu sản phẩm trả phí tiếp theo không? |
| **Opt-in Friction** (Ma sát điền form) | 0-10 | Form đăng ký có đơn giản không? (10 = chỉ yêu cầu điền duy nhất Email) |

**Thứ tự hiệu quả của các loại Lead Magnet từ cao xuống thấp:**
1. Các công cụ tính toán và biểu mẫu mẫu (tỷ lệ chuyển đổi cao nhất, trao giá trị sử dụng được ngay).
2. Checklist và tài liệu tóm tắt nhanh (dễ tiêu thụ, áp dụng nhanh).
3. Case study thực tế có số liệu (xây dựng uy tín mạnh mẽ).
4. Các buổi đào tạo bằng video hoặc workshop (giá trị cảm nhận cao).
5. Ebook và sách hướng dẫn (tỷ lệ chuyển đổi thấp hơn nhưng tốt để xây dựng chuyên gia).
6. Bài test trắc nghiệm đánh giá (mang tính tương tác, tỷ lệ tham gia cao).
7. Dùng thử miễn phí hoặc xem demo (định hướng bằng sản phẩm trực tiếp, ý định mua hàng cao nhất).

---

## Giai đoạn 3: Chỉ số đo lường Phễu và Benchmarks

### 3.1 Chỉ số KPIs chính của Phễu

Tính toán (hoặc ước lượng dựa trên số liệu thực tế của ngành) các chỉ số sau:

```
CHỈ SỐ ĐO LƯỜNG PHỄU (FUNNEL METRICS)
====================================

Chỉ số traffic:
  Lượng truy cập hàng tháng: [số liệu thực tế hoặc ước tính]
  Nguồn traffic: [organic %, paid %, referral %, direct %, social %]

Chỉ số chuyển đổi:
  Khách truy cập → Đăng ký Lead: [X]% (benchmark: 2-5%)
  Lead → Lead chất lượng (MQL): [X]% (benchmark: 15-30%)
  MQL → Cơ hội mua hàng: [X]% (benchmark: 30-50%)
  Cơ hội → Trở thành khách hàng: [X]% (benchmark: 20-40%)
  Chuyển đổi chung (Visitor → Customer): [X]% (benchmark: 0.5-3%)

Chỉ số doanh thu:
  Giá trị đơn hàng trung bình (AOV): $[X]
  Giá trị trọn đời khách hàng (LTV): $[X]
  Chi phí thu hút khách hàng (CAC): $[X]
  Tỷ lệ LTV:CAC Ratio: [X]:1 (mục tiêu tối ưu: 3:1 hoặc cao hơn)
  Doanh thu trên mỗi lượt truy cập (RPV): $[X]

Chỉ số tương tác:
  Số trang xem mỗi phiên: [X]
  Thời gian phiên trung bình: [X] phút
  Tỷ lệ thoát (Bounce Rate): [X]% (benchmark: 30-60%)
```

### 3.2 Cách tính toán chỉ số Doanh thu trên lượt truy cập (RPV)

Đây là chỉ số quan trọng bậc nhất khi tối ưu hóa phễu bán hàng:

```
RPV = Tổng doanh thu tháng / Tổng lượng khách truy cập tháng

Ví dụ thực tế:
  10,000 visitors/tháng x 2% tỷ lệ chuyển đổi x $100 AOV = $20,000/tháng
  RPV = $20,000 / 10,000 = $2.00 trên mỗi lượt truy cập

Nếu chúng ta tối ưu phễu tăng tỷ lệ chuyển đổi từ 2% lên 2.5%:
  10,000 visitors x 2.5% x $100 = $25,000/tháng
  RPV mới = $2.50 trên mỗi lượt truy cập
  Doanh thu tăng thêm = $5,000/tháng = $60,000/năm
```

Áp dụng khung tính toán này để định lượng hóa giá trị thực tế của từng đề xuất cải tiến.

### 3.3 Chỉ số chuyển đổi Benchmark theo từng loại Phễu

| Loại phễu | Tỷ lệ Tốt (Good) | Tỷ lệ Rất tốt (Great) | Tỷ lệ Xuất sắc (Elite) |
|-------------|----------------|-----------------|-----------------|
| Lead Gen (điền form) | 3-5% | 5-10% | 10-20% |
| SaaS Free Trial (đăng ký thử) | 2-5% | 5-10% | 10-15% |
| Dùng thử chuyển sang Trả phí | 10-15% | 15-25% | 25-40% |
| E-commerce (truy cập -> mua) | 1-3% | 3-5% | 5-8% |
| Giỏ hàng -> Mua hàng thành công | 50-60% | 60-70% | 70-80% |
| Đăng ký Webinar | 20-40% | 40-55% | 55-70% |
| Tham gia Webinar thực tế | 30-40% | 40-55% | 55-65% |
| Mua hàng từ Webinar | 2-5% | 5-10% | 10-20% |
| Phản hồi Email lạnh | 3-5% | 5-10% | 10-20% |
| Xem demo chốt đơn thành công | 15-25% | 25-40% | 40-60% |

---

## Giai đoạn 4: Đề xuất Tối ưu hóa Phễu

### 4.1 Ma trận ưu tiên hành động

Xếp hạng các đề xuất tối ưu hóa theo khung phân loại:

| Mức độ ưu tiên | Tác động dự kiến | Nỗ lực triển khai | Khung thời gian |
|----------|--------|--------|-------------------|
| **P1 (Làm Ngay)** | Tác động Cao (>10% tăng trưởng) | Nỗ lực thấp (<1 ngày làm việc) | Trong tuần này |
| **P2 (Lên Kế hoạch)** | Tác động Cao (>10% tăng trưởng) | Nỗ lực vừa (1-5 ngày làm việc) | Trong tháng này |
| **P3 (Sắp xếp lịch)** | Tác động Vừa (5-10% tăng trưởng) | Nỗ lực thấp (<1 ngày làm việc) | Trong tháng này |
| **P4 (Đưa vào Backlog)** | Tác động Vừa (5-10% tăng trưởng) | Nỗ lực cao (trên 5 ngày làm việc) | Trong quý này |
| **P5 (Tùy chọn)** | Tác động Thấp (<5% tăng trưởng) | Mọi mức độ nỗ lực | Khi có dư tài nguyên |

### 4.2 Các hạng mục tối ưu hóa theo giai đoạn Phễu

**Đầu phễu TOFU (Nhận diện sang Thích thú):**
- Thử nghiệm A/B Test Headline chính (tác động dự kiến: cải thiện 10-30%)
- Bố trí lại vị trí đặt các Social Proof (tác động dự kiến: 5-15%)
- Tối ưu hóa tốc độ tải trang (tác động dự kiến: 5-20%)
- Triển khai popup bắt giữ khách có ý định thoát kèm Lead Magnet (tác động dự kiến: 2-5%)

**Giữa phễu MOFU (Thích thú sang Xem xét):**
- Xây dựng trang case study và testimonial chuyên sâu (tác động dự kiến: 10-20%)
- Xây dựng trang so sánh tính năng đối thủ (tác động dự kiến: 5-15%)
- Xây dựng trải nghiệm demo dùng thử tương tác trực quan (tác động dự kiến: 15-30%)
- Triển khai chuỗi email nuôi dưỡng tiếp thị lại (tác động dự kiến: 10-25%)

**Đáy phễu BOFU (Xem xét sang Mua hàng):**
- Thiết kế lại trang bảng giá (tác động dự kiến: 10-25%)
- Loại bỏ ma sát tại trang thanh toán (tác động dự kiến: 5-15%)
- Áp dụng các cam kết bảo hành loại bỏ rủi ro (tác động dự kiến: 10-20%)
- Thêm các yếu tố giới hạn khẩn cấp chân thực (tác động dự kiến: 5-15%)
- Khôi phục giỏ hàng bỏ quên tự động (tác động dự kiến khôi phục: 5-15%)

**Sau mua hàng (Giữ chân và Mở rộng):**
- Triển khai chuỗi email Onboarding hướng dẫn sử dụng (giảm 10-20% tỷ lệ rời bỏ)
- Đưa gợi ý bán thêm (upsell/cross-sell) ngay tại trang cảm ơn (tăng 5-15% giá trị đơn AOV)
- Triển khai chương trình giới thiệu bạn bè nhận quà (referral) (tăng 5-15% lượng khách mới)
- Thực hiện khảo sát NPS đo lường độ hài lòng sau 30 ngày sử dụng

---

## Giai đoạn 5: Tích hợp chuỗi Email Nuôi dưỡng

### 5.1 Khớp nối Phễu với Chuỗi Email

Đối với từng giai đoạn trong phễu, hãy thiết lập chuỗi Email tương ứng:

```
Giai đoạn của Phễu          → Chuỗi Email phù hợp
--------------------------------------------------
Visitor (Chưa biết thông tin) → Không gửi (Sử dụng ad retargeting tiếp thị lại)
Lead (Đã đăng ký nhận tin)    → Welcome sequence (5-7 email)
Engaged Lead (Tương tác tốt)  → Nurture sequence (6-8 email)
Trial User (Đang dùng thử)    → Onboarding sequence (5-7 email)
Inactive Trial (Ngừng dùng)   → Re-engagement sequence (3-4 email)
Customer (Khách mua hàng)     → Post-purchase / Loyalty sequence
Churned Customer (Rời bỏ)     → Win-back sequence (3-4 email)
```

### 5.2 Đồng bộ nguồn Traffic với Điểm chạm Phễu

Mỗi nguồn traffic mang mức ý định mua hàng khác nhau cần được trỏ tới điểm chạm phễu phù hợp:

| Nguồn Traffic | Mức độ ý định | Điểm tiếp cận tối ưu | Phễu khuyên dùng |
|---------------|-------------|-----------------|-------------------|
| Tìm kiếm thương hiệu | Rất cao | Trang bảng giá / Đăng ký trực tiếp | Phễu ngắn (chuyển đổi thẳng) |
| Tìm kiếm từ khóa ngành | Trung bình | Bài viết blog / Landing page giải pháp | Phễu vừa (giáo dục trước rồi convert) |
| Quảng cáo MXH | Thấp - Vừa | Nhận Lead Magnet / Tài liệu hữu ích | Phễu dài (thu thập email, nuôi dưỡng, convert) |
| Trang giới thiệu bên ngoài | Trung bình - Cao | Trang chủ / Trang sản phẩm | Phễu vừa (lợi dụng lòng tin có sẵn) |
| Truy cập trực tiếp | Cao | Trang chủ | Phễu ngắn |
| Qua Email marketing | Trung bình | Landing page chuyên biệt theo chủ đề | Phễu được nhắm mục tiêu chính xác |

---

## Định dạng Đầu ra: FUNNEL-ANALYSIS.md

Ghi toàn bộ kết quả phân tích vào file `FUNNEL-ANALYSIS.md`:

```markdown
# Phân tích Phễu Bán hàng Bitsness: [Tên doanh nghiệp]
**URL:** [url]
**Ngày thực hiện:** [ngày tháng hiện tại]
**Mô hình kinh doanh:** [loại mô hình]
**Loại phễu áp dụng:** [loại phễu]
**Điểm sức khỏe phễu tổng thể: [X]/100**

---

## Tóm tắt Điều hành (Executive Summary)
[Đoạn tóm tắt từ 3-4 đoạn bao gồm: phân loại phễu, đánh giá hiệu suất hiện tại, điểm nghẽn lớn nhất của phễu, top 3 khuyến nghị hành động tối ưu kèm theo ước lượng doanh thu tăng thêm.]

---

## Sơ đồ Phễu chuyển đổi
[Sơ đồ phễu dạng text-based biểu diễn tỷ lệ chuyển đổi ước tính qua từng bước]

---

## Phân tích chi tiết từng bước hành trình

### Bước 1: [Tên trang]
[Phân tích đầy đủ kèm điểm số, các điểm ma sát phát hiện, tín hiệu uy tín đang có và đề xuất tối ưu.]

### Bước 2: [Tên trang]
[Lặp lại cho các bước tiếp theo trong hành trình]

---

## Chỉ số KPIs của Phễu
[Bảng tổng hợp chỉ số hiện tại đối chiếu với benchmark của ngành, chỉ rõ các khoảng trống hiệu suất.]

## Ước tính tác động Doanh thu
[Tính toán chi tiết RPV, các kịch bản tăng trưởng khi tối ưu tỷ lệ chuyển đổi.]

## Khuyến nghị tối ưu hóa phễu

### Ưu tiên 1 — Làm Ngay (Trong tuần này)
[Các đầu việc cụ thể kèm theo tăng trưởng chuyển đổi ước tính]

### Ưu tiên 2 — Lên Kế hoạch (Trong tháng này)
[Các đầu việc cần lên kế hoạch triển khai]

### Ưu tiên 3 — Chiến lược dài hạn (Trong quý này)
[Các đầu việc mang tính chiến lược hệ thống]

---

## Đánh giá chi tiết Trang bảng giá
[Phần kiểm tra chi tiết trang bảng giá kèm theo checklist]

## Đánh giá hiệu quả của Lead Magnet
[Nếu có: chấm điểm chi tiết và các khuyến nghị cải tiến mồi dẫn dụ]

## Tích hợp chuỗi Email Marketing chăm sóc
[Các chuỗi email đề xuất tương ứng với từng giai đoạn phễu khách hàng]

## Đồng bộ điểm chạm nguồn Traffic
[Định hướng phân bổ luồng traffic đến các trang đích tối ưu]

---

## Các bước tiếp theo cần làm
1. [Hành động tối ưu khẩn cấp nhất]
2. [Hành động ưu tiên thứ hai]
3. [Hành động ưu tiên thứ ba]
```

---

## Định dạng hiển thị ở Terminal

```
=== HOÀN THÀNH PHÂN TÍCH PHỄU BITSNESS ===

Doanh nghiệp: [name]
Loại phễu: [type]
Số bước hành trình: [count]
Điểm sức khỏe phễu: [X]/100

Luồng chuyển đổi thực tế:
  Visitor      → Lead Mới:   [X]% (mức benchmark: [X]%)
  Lead         → Dùng thử:   [X]% (mức benchmark: [X]%)
  Dùng thử     → Trả phí:    [X]% (mức benchmark: [X]%)
  Tỷ lệ chung:               [X]% (mức benchmark: [X]%)

Điểm nghẽn lớn nhất: Giai đoạn [stage] — Tỷ lệ rơi rớt [X]%
Cơ hội doanh thu: tăng thêm $[X,XXX]/tháng sau khi xử lý các điểm nghẽn

Top 3 Hành động Cần làm ngay:
  1. [sửa đổi] — Tăng chuyển đổi ước tính [X]%
  2. [sửa đổi] — Tăng chuyển đổi ước tính [X]%
  3. [sửa đổi] — Tăng chuyển đổi ước tính [X]%

Báo cáo phân tích đầy đủ đã được lưu tại: FUNNEL-ANALYSIS.md
```

---

## Tích hợp chéo giữa các kỹ năng

- Nếu file `MARKETING-AUDIT.md` đã có sẵn, hãy đối chiếu điểm số của danh mục Conversion Optimization trong đó.
- Nếu file `COPY-SUGGESTIONS.md` đã có sẵn, hãy cập nhật các đề xuất chỉnh sửa copy vào các trang đích trong phễu.
- Nếu file `EMAIL-SEQUENCES.md` đã có sẵn, hãy xác minh mức độ đồng bộ với các bước hành trình của phễu.
- Nếu file `COMPETITOR-REPORT.md` đã có sẵn, hãy so sánh hiệu quả phễu chuyển đổi của bạn với đối thủ cạnh tranh.
- Gợi ý câu lệnh tiếp theo: chạy lệnh `/market copy` để viết lại nội dung các trang, chạy lệnh `/market emails` để tạo các chuỗi email chăm sóc tương ứng, chạy lệnh `/market landing` để tối ưu hóa chuyên sâu Landing Page.
