# Tạo Báo cáo Marketing (Định dạng Markdown)

## Mục tiêu Kỹ năng

Tạo ra một báo cáo marketing toàn diện, được định dạng chuyên nghiệp bằng Markdown. Kỹ năng này tổng hợp dữ liệu từ tất cả các kết quả audit và phân tích trước đó thành một tài liệu duy nhất gửi khách hàng, bao gồm các điểm số đánh giá, phát hiện chính, khuyến nghị cải tiến và một kế hoạch hành động theo thứ tự ưu tiên kèm theo ước tính tác động doanh thu.

## Khi nào sử dụng

- Người dùng muốn có một báo cáo marketing đầy đủ cho khách hàng hoặc cho chính doanh nghiệp của họ.
- Người dùng đã hoàn thành một hoặc nhiều bước audit trước đó và muốn tổng hợp lại thành báo cáo.
- Người dùng yêu cầu đánh giá marketing, bảng điểm marketing hoặc tài liệu phân tích.
- Được kích hoạt bởi lệnh `/market report` hoặc `/market report <domain>`.

## Hướng dẫn thực hiện

### Bước 1: Thu thập tất cả dữ liệu có sẵn

Trước khi tạo báo cáo, hãy kiểm tra xem trong thư mục dự án đã có sẵn dữ liệu phân tích nào từ các lệnh chạy trước đó chưa. Tìm các file sau:

**Các nguồn dữ liệu có thể có:**
- `MARKETING-AUDIT.md` -- tạo từ lệnh `/market audit`
- `LANDING-CRO.md` -- tạo từ lệnh `/market landing`
- `SEO-AUDIT.md` -- tạo từ lệnh `/market seo`
- `BRAND-VOICE.md` -- tạo từ lệnh `/market brand`
- `COMPETITOR-ANALYSIS.md` -- tạo từ lệnh `/market competitors`
- `FUNNEL-ANALYSIS.md` -- tạo từ lệnh `/market funnel`
- `CONTENT-AUDIT.md` -- tạo từ phân tích nội dung
- `AD-AUDIT.md` -- tạo từ lệnh `/market ads`
- `SOCIAL-AUDIT.md` -- tạo từ lệnh `/market social`
- `EMAIL-AUDIT.md` -- tạo từ lệnh `/market emails`

Nếu chưa có dữ liệu nào trước đó, hãy thông báo cho người dùng và đề xuất:
1. Chạy một chiến dịch audit nhanh trước (khuyên dùng).
2. Tạo báo cáo dựa trên các thông tin hiện có (quét URL website, dữ liệu do người dùng cung cấp).
3. Tạo một biểu mẫu báo cáo trống để họ tự điền thông tin.

### Bước 2: Tính toán Bảng điểm Marketing Scorecard

Chấm điểm trên 6 danh mục chính, mỗi danh mục tối đa 100 điểm. Điểm số tổng thể được tính bằng trung bình cộng có trọng số.

#### Danh mục 1: Website & Conversion (Trọng số: 25%)
Đánh giá dựa trên phân tích Landing Page, các phát hiện CRO và trải nghiệm UX.

| Yếu tố đánh giá | Điểm tối đa | Tiêu chí chấm điểm |
|---|---|---|
| Tốc độ tải trang | 15 | Dưới 2 giây = 15, Dưới 3 giây = 10, Dưới 5 giây = 5, Trên 5 giây = 0 |
| Hiển thị di động (Mobile) | 15 | Hoàn toàn tương thích = 15, Phần lớn = 10, Một phần = 5, Không tương thích = 0 |
| Value Proposition rõ ràng | 20 | Rõ ràng ngay lập tức = 20, Cần thời gian hiểu = 12, Mơ hồ = 5, Thiếu = 0 |
| Hiệu quả nút CTA | 20 | Mạnh mẽ và rõ ràng = 20, Có nút nhưng yếu = 12, Mơ hồ = 5, Thiếu = 0 |
| Social Proof | 15 | Có nhiều loại hình = 15, Có một số = 10, Rất ít = 5, Không có = 0 |
| Tối ưu hóa Form đăng ký | 15 | Tối ưu tốt = 15, Chấp nhận được = 10, Cần cải thiện = 5, Bị lỗi = 0 |

#### Danh mục 2: SEO & Organic (Trọng số: 20%)
Đánh giá dựa trên các phát hiện của chiến dịch audit SEO.

| Yếu tố đánh giá | Điểm tối đa | Tiêu chí chấm điểm |
|---|---|---|
| Thẻ Title & Meta Description | 15 | Được tối ưu = 15, Có thẻ nhưng chưa tối ưu = 10, Một phần = 5, Thiếu thẻ = 0 |
| Phân cấp tiêu đề H1-H6 | 10 | Phân cấp đúng chuẩn = 10, Đúng phần lớn = 7, Cần tối ưu = 3, Không phân cấp = 0 |
| Chất lượng nội dung (E-E-A-T) | 25 | Xuất sắc = 25, Tốt = 17, Trung bình = 10, Yếu kém = 3 |
| Kỹ thuật SEO (Technical SEO) | 20 | Không có lỗi = 20, Lỗi nhỏ = 13, Lỗi lớn = 7, Lỗi nghiêm trọng = 0 |
| Liên kết nội bộ (Internal link) | 15 | Có chiến lược tốt = 15, Có liên kết = 10, Rất ít = 5, Không có = 0 |
| Đánh dấu Schema | 15 | Đầy đủ chuyên sâu = 15, Cơ bản = 10, Rất ít = 5, Không có = 0 |

#### Danh mục 3: Content & Messaging (Trọng số: 15%)
Đánh giá dựa trên phân tích Brand Voice và audit nội dung.

| Yếu tố đánh giá | Điểm tối đa | Tiêu chí chấm điểm |
|---|---|---|
| Nhất quán Brand Voice | 20 | Đồng bộ nhất quán = 20, Đồng bộ phần lớn = 13, Thiếu nhất quán = 7, Không có cá tính = 0 |
| Chất lượng bài viết | 25 | Chuẩn chuyên gia = 25, Tốt = 17, Viết chung chung = 10, Yếu kém = 3 |
| Đa dạng định dạng | 15 | Nhiều định dạng khác nhau = 15, Có vài loại = 10, Hạn chế = 5, Chỉ có 1 loại = 0 |
| Tần suất xuất bản | 15 | Đăng đều đặn = 15, Thỉnh thoảng = 10, Rất hiếm = 5, Không đăng bài = 0 |
| Nhắm mục tiêu đối tượng | 25 | Nhắm trúng mục tiêu = 25, Nhắm tương đối = 17, Tệp quá rộng = 10, Lệch mục tiêu = 3 |

#### Danh mục 4: Social Media & Community (Trọng số: 15%)
Đánh giá dựa trên sự hiện diện và tương tác trên mạng xã hội.

| Yếu tố đánh giá | Điểm tối đa | Tiêu chí chấm điểm |
|---|---|---|
| Sự hiện diện trên nền tảng | 15 | Chọn đúng kênh & active = 15, Có kênh nhưng bỏ không = 8, Thiếu kênh cốt lõi = 3 |
| Chất lượng nội dung đăng | 25 | Tương tác tốt & đúng brand = 25, Chấp nhận được = 15, Chất lượng kém = 7, Rất tệ = 0 |
| Tỷ lệ tương tác (Engagement) | 25 | Trên mức benchmark = 25, Đạt benchmark = 17, Dưới mức = 10, Không đáng kể = 3 |
| Nhất quán lịch đăng bài | 15 | Đăng bài đều đặn = 15, Sporadic = 10, Rất hiếm = 5, Đã bỏ xó = 0 |
| Xây dựng cộng đồng | 20 | Cộng đồng hoạt động mạnh = 20, Có tương tác = 13, Chỉ đăng một chiều = 7, Không có = 0 |

#### Danh mục 5: Email & Automation (Trọng số: 15%)
Đánh giá dựa trên hệ thống Email Marketing.

| Yếu tố đánh giá | Điểm tối đa | Tiêu chí chấm điểm |
|---|---|---|
| Cơ chế thu thập Email | 20 | Nhiều điểm đăng ký opt-in = 20, Chỉ có 1 điểm = 13, Không có điểm thu thập nào = 5 |
| Thiết kế & Nội dung email | 20 | Chuyên nghiệp cuốn hút = 20, Chấp nhận được = 13, Cần cải thiện = 7 |
| Chuỗi tự động hóa (Automation) | 25 | Đầy đủ chuyên sâu = 25, Cơ bản = 15, Rất ít = 8, Không có = 0 |
| Phân khúc danh sách (Segmentation) | 20 | Phân khúc nâng cao = 20, Phân khúc cơ bản = 13, Không phân khúc = 5 |
| Tín hiệu khả năng gửi (Deliverability) | 15 | Tín hiệu mạnh = 15, Đạt yêu cầu = 10, Đáng lo ngại = 5, Gặp lỗi gửi = 0 |

#### Danh mục 6: Paid Advertising (Trọng số: 10%)
Đánh giá dựa trên kiểm tra tài khoản quảng cáo Ads (nếu áp dụng).

| Yếu tố đánh giá | Điểm tối đa | Tiêu chí chấm điểm |
|---|---|---|
| Cấu trúc chiến dịch | 20 | Tổ chức tốt bài bản = 20, Đạt yêu cầu = 13, Lộn xộn = 7, Không chạy ads = 0 |
| Chất lượng nhắm mục tiêu | 25 | Nhắm trúng mục tiêu & phân lớp = 25, Tốt = 17, Quá rộng = 10, Lãng phí ngân sách = 3 |
| Chất lượng mẫu quảng cáo | 25 | Cuốn hút & đa dạng = 25, Đạt yêu cầu = 17, Yếu kém = 10, Rất tệ = 3 |
| Đồng bộ trang đích (Landing Page) | 15 | Đồng bộ hoàn hảo = 15, Khớp tương đối = 10, Lệch thông điệp = 5, Link lỗi = 0 |
| Tracking & attribution | 15 | Đầy đủ chuyên sâu = 15, Cơ bản = 10, Rất sơ sài = 5, Thiếu tracking = 0 |

#### Công thức tính Điểm số tổng thể
```
Overall Score = (Website & Conversion * 0.25) + (SEO & Organic * 0.20) + (Content & Messaging * 0.15) + (Social Media * 0.15) + (Email & Automation * 0.15) + (Paid Advertising * 0.10)
```

**Cách đọc thang điểm:**
| Khoảng điểm | Đánh giá | Ý nghĩa |
|---|---|---|
| 85-100 | Xuất sắc | Hoạt động marketing là lợi thế cạnh tranh. Tiếp tục tối ưu và scale. |
| 70-84 | Tốt | Nền tảng vững chắc với các cơ hội cải tiến rõ ràng. |
| 55-69 | Trung bình | Hoạt động bình thường nhưng đang bỏ lỡ nhiều cơ hội tăng trưởng lớn. |
| 40-54 | Dưới trung bình | Nhiều mảng cần lưu ý sửa đổi. Chi phí cơ hội bị thất thoát lớn. |
| 0-39 | Yếu kém | Hoạt động marketing đang làm hại tới tăng trưởng. Cần hành động ngay lập tức. |

### Bước 3: Viết phân tích sâu từng Danh mục

Đối với mỗi danh mục trong 6 danh mục trên, cung cấp:
1. **Điểm số và Đánh giá** -- X/100 kèm theo diễn giải.
2. **Phát hiện chính** -- 3-5 quan sát cụ thể có dẫn chứng rõ ràng.
3. **Các điểm đang làm tốt** -- Các yếu tố tích cực cần phát huy.
4. **Lỗ hổng & Điểm yếu** -- Các vấn đề phát hiện kèm theo mức độ nghiêm trọng.
5. **Khuyến nghị tối ưu** -- Đề xuất sửa đổi cụ thể được xếp hạng theo tác động.
6. **Ước tính Tác động Doanh thu** -- Định lượng doanh số tăng thêm khi sửa đổi.

**Khung tính toán Tác động Doanh thu:**
```
Doanh thu tăng thêm = (Thay đổi traffic ước tính * Thay đổi tỷ lệ chuyển đổi * Giá trị đơn hàng trung bình) * Chỉ số tin cậy

Ví dụ minh họa:
- Traffic hàng tháng hiện tại: 10,000
- Đề xuất tối ưu SEO giúp tăng traffic thêm 30%: +3,000 traffic
- Tỷ lệ chuyển đổi hiện tại: 2%, tối ưu CRO giúp tăng lên 3%: chênh lệch +1% = +130 lượt chuyển đổi mới
- Giá trị đơn hàng trung bình (AOV): $500
- Tác động doanh thu hàng tháng ước tính: $65,000
- Chỉ số tin cậy (Mức thận trọng): 0.5
- Doanh thu thực tế ước tính tăng thêm: $32,500/tháng
```

### Bước 4: Tóm tắt So sánh đối thủ cạnh tranh

Nếu đã có dữ liệu đối thủ từ lệnh `/market competitors`, hãy đưa vào báo cáo:

**Ma trận Định vị Cạnh tranh:**
| Tiêu chí | Khách hàng | Đối thủ 1 | Đối thủ 2 | Đối thủ 3 |
|---|---|---|---|---|
| Chất lượng Website | X/10 | X/10 | X/10 | X/10 |
| Sự hiện diện SEO | X/10 | X/10 | X/10 | X/10 |
| Chất lượng nội dung | X/10 | X/10 | X/10 | X/10 |
| Sự hiện diện MXH | X/10 | X/10 | X/10 | X/10 |
| Vị thế tổng thể | Thứ X/4 | Thứ X/4 | Thứ X/4 | Thứ X/4 |

**Lợi thế cạnh tranh:** Những điểm khách hàng làm tốt hơn đối thủ.
**Lỗ hổng cạnh tranh:** Những điểm đối thủ đang làm vượt trội hơn khách hàng.
**Cơ hội cạnh tranh:** Các thị phần ngách đối thủ chưa tiếp cận tốt.

### Bước 5: Đánh giá Chất lượng Nội dung (Content Quality)

Tóm tắt các phát hiện về nội dung trên tất cả các kênh:
- **Copywriting trên website** -- Tính rõ ràng, sức thuyết phục, độ đồng bộ thương hiệu.
- **Nội dung Blog** -- Độ sâu bài viết, tính chuyên môn, tối ưu SEO, tần suất đăng.
- **Nội dung Mạng xã hội** -- Tỷ lệ tương tác, sự nhất quán thương hiệu, tối ưu kênh.
- **Nội dung Email** -- Sự cuốn hút của tiêu đề, chất lượng nội dung thư, sức mạnh CTA.
- **Ý tưởng quảng cáo Ads** -- Sự rõ ràng của thông điệp, chất lượng hình ảnh thiết kế, cách đưa ưu đãi.

### Bước 6: Tóm tắt Tối ưu hóa Chuyển đổi (CRO)

Tổng hợp tất cả các phát hiện liên quan đến chuyển đổi:
- **Đường dẫn chuyển đổi chính** -- Cách khách truy cập trở thành khách mua hàng.
- **Rò rỉ phễu (Funnel leaks)** -- Các điểm khách hàng rời đi nhiều nhất.
- **CRO Quick Wins** -- Các chỉnh sửa nhỏ có thể thực hiện được ngay để tăng chuyển đổi.
- **Cơ hội thử nghiệm** -- Các giả thuyết đề xuất cho chương trình chạy thử nghiệm A/B Test.
- **So sánh chỉ số benchmark** -- Tỷ lệ hiện tại đối chiếu với trung bình ngành.

### Bước 7: Ảnh chụp nhanh SEO (SEO Snapshot)

Tóm tắt sức khỏe SEO dưới định dạng trực quan dễ đọc:

```
Ảnh chụp nhanh SEO:
- Thẻ Title: [Được tối ưu / Chưa tối ưu / Thiếu]
- Thẻ Meta Description: [Được tối ưu / Chưa tối ưu / Thiếu]
- Thẻ H1: [Đúng chuẩn / Gặp lỗi / Thiếu]
- Thẻ Alt hình ảnh: [Đầy đủ / Một phần / Thiếu]
- Tốc độ trang: [Nhanh / Vừa phải / Chậm]
- Thân thiện di động: [Có / Một phần / Chưa]
- Đánh dấu Schema: [Có / Một phần / Chưa]
- File Robots.txt: [Đã cấu hình / Có lỗi / Chưa có]
- File Sitemap: [Đã cấu hình / Có lỗi / Chưa có]
- Bảo mật HTTPS: [Có / Chưa]
- Core Web Vitals: [Đạt / Cần tối ưu / Yếu]
```

### Bước 8: Lập kế hoạch hành động theo thứ tự ưu tiên

Phân chia toàn bộ các khuyến nghị cải tiến thành 3 cấp độ:

#### Chiến thắng nhanh (Quick Wins) (Thực hiện trong tuần này)
Các thay đổi đem lại tác động cao nhưng tốn ít công sức thực hiện (thời gian làm từ 1-5 ngày).

Mỗi đầu việc định dạng theo mẫu:
```
- [ ] [Đầu việc cần làm]: [Mô tả chi tiết đầu việc]
  - Tác động: [HIGH/MEDIUM/LOW]
  - Nỗ lực thực hiện: [1-5 giờ làm việc]
  - Kết quả kỳ vọng: [Mô tả kết quả đạt được]
  - Tác động doanh thu: [Ước tính $X/tháng]
```

#### Trung hạn (Thực hiện trong tháng này)
Các thay đổi đòi hỏi công sức và tác động ở mức vừa phải, cần từ 1-4 tuần để hoàn thành.

#### Chiến lược (Thực hiện trong quý này)
Các thay đổi lớn mang tính nền tảng, tác động cao, đòi hỏi nỗ lực thực hiện dài hơi và có kế hoạch bài bản.

### Bước 9: Thiết lập Lộ trình Roadmap 30-60-90 ngày

**Ngày 1-30: Thiết lập Nền tảng & Quick Wins**
- Tuần 1: Triển khai toàn bộ các đầu việc Quick Wins trong kế hoạch hành động.
- Tuần 2: Thiết lập hệ thống đo lường và theo dõi chỉ số nền tảng.
- Tuần 3: Bắt đầu triển khai các đầu việc cải tiến trung hạn.
- Tuần 4: Đánh giá hiệu suất tháng đầu tiên và điều chỉnh chiến thuật.

**Ngày 31-60: Tăng trưởng & Tối ưu hóa**
- Tuần 5-6: Triển khai các nâng cấp cho các chiến dịch quảng cáo chính.
- Tuần 7: Bắt đầu chương trình chạy thử nghiệm A/B Test.
- Tuần 8: Bắt tay triển khai chiến lược nội dung mới.

**Ngày 61-90: Tăng quy mô & Mở rộng (Scale)**
- Tuần 9-10: Đẩy mạnh các mảng hiệu quả, cắt giảm mảng kém tối ưu.
- Tuần 11: Mở rộng chiến dịch sang các kênh truyền thông mới.
- Tuần 12: Tổng kết đánh giá quý, cập nhật định hướng chiến lược cho quý sau.

---

## Định dạng Đầu ra: MARKETING-REPORT.md

Lưu báo cáo hoàn chỉnh vào file `MARKETING-REPORT.md` với cấu trúc:

```markdown
# Báo cáo Phân tích Marketing toàn diện

## Doanh nghiệp: [Tên công ty / Domain]
### Được thực hiện bởi: [Bitsness / Tên Agency]
### Ngày thực hiện: [Ngày tháng]

---

## Tóm tắt Điều hành (Executive Summary)

### Điểm Marketing tổng thể: [X/100] -- [Đánh giá hạng]

[Đoạn tóm tắt từ 2-3 đoạn bao gồm: đánh giá hiện trạng, top 3 phát hiện quan trọng nhất, ước tính tác động doanh thu khi cải tiến và các bước khuyến nghị đầu tiên.]

### Điểm số chi tiết theo danh mục
| Danh mục đánh giá | Điểm số | Phân loại |
|---|---|---|
| Website & Conversion | X/100 | [Phân loại] |
| SEO & Organic | X/100 | [Phân loại] |
| Content & Messaging | X/100 | [Phân loại] |
| Social Media | X/100 | [Phân loại] |
| Email & Automation | X/100 | [Phân loại] |
| Paid Advertising | X/100 | [Phân loại] |
| **ĐIỂM TỔNG THỂ** | **X/100** | **[Phân loại]** |

### Top 3 Hành động Ưu tiên hàng đầu
1. [Khuyến nghị tác động lớn nhất kèm con số doanh thu ước tính]
2. [Khuyến nghị ưu tiên thứ hai]
3. [Khuyến nghị ưu tiên thứ ba]

---

## Phân tích chi tiết từng danh mục

### 1. Website & Conversion [Điểm số: X/100]
[Phân tích chuyên sâu: phát hiện, điểm làm tốt, lỗ hổng cần sửa, các đề xuất cụ thể]

### 2. SEO & Organic [Điểm số: X/100]
[Phân tích chuyên sâu]

### 3. Content & Messaging [Điểm số: X/100]
[Phân tích chuyên sâu]

### 4. Social Media [Điểm số: X/100]
[Phân tích chuyên sâu]

### 5. Email & Automation [Điểm số: X/100]
[Phân tích chuyên sâu]

### 6. Paid Advertising [Điểm số: X/100]
[Phân tích chuyên sâu]

---

## So sánh vị thế với Đối thủ cạnh tranh
[Ma trận so sánh và các phân tích khác biệt]

---

## Ảnh chụp nhanh SEO (SEO Snapshot)
[Bảng checklist sức khỏe SEO]

---

## Tóm tắt Tối ưu hóa Chuyển đổi (CRO)
[Bản phân tích phễu và các khuyến nghị tối ưu hóa chuyển đổi]

---

## Bảng tổng hợp tác động Doanh thu
| Khuyến nghị cải tiến | Tác động doanh thu hàng tháng ước tính | Mức độ tin cậy | Thứ tự ưu tiên |
|---|---|---|---|
| [Khuyến nghị 1] | $X,XXX | Cao/Vừa/Thấp | 1 |
| [Khuyến nghị 2] | $X,XXX | Cao/Vừa/Thấp | 2 |
| ... | ... | ... | ... |
| **Tổng doanh thu tăng thêm ước tính** | **$XX,XXX/tháng** | | |

---

## Kế hoạch hành động theo thứ tự ưu tiên

### Chiến thắng nhanh (Quick Wins - Thực hiện trong tuần này)
- [ ] [Các đầu việc cụ thể kèm thông số tác động và nỗ lực]

### Trung hạn (Thực hiện trong tháng này)
- [ ] [Các đầu việc]

### Dài hạn (Thực hiện trong quý này)
- [ ] [Các đầu việc]

---

## Lộ trình phát triển Roadmap 30-60-90 ngày
[Kế hoạch triển khai từng tuần]

---

## Phụ lục
### Phương pháp đánh giá & Chấm điểm
### Các công cụ và script sử dụng
### Thuật ngữ định nghĩa chuyên ngành (Glossary)
### Các nguồn dữ liệu phân tích
```

## Các nguyên tắc cốt lõi

- Bản báo cáo này phải được trình bày cực kỳ chỉn chu để có thể làm tài liệu bán hàng chuyên nghiệp. Một bản báo cáo chất lượng cao sẽ mở toang cánh cửa hợp tác lâu dài với khách hàng.
- Luôn dẫn dắt người đọc bằng các insight và cơ hội phát triển, tránh lối chỉ trích chê bai. Hãy định khung mọi lỗi sai dưới góc nhìn của "tiềm năng tăng trưởng".
- Định lượng hóa mọi số liệu có thể. Con số "$32,000/tháng doanh thu chưa được khai thác" luôn mang tính thuyết phục cực kỳ cao hơn so với câu nói chung chung "bên mình đang bỏ lỡ nhiều tiền".
- Thiết lập kế hoạch hành động cụ thể để một marketer tập sự cũng có thể cầm tài liệu và tự triển khai được.
- Sử dụng nhất quán font chữ, định dạng bảng biểu rõ ràng và hệ thống phân cấp thị giác chuyên nghiệp của Bitsness.
