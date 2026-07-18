# Tạo Báo cáo Marketing dạng PDF (PDF Report Generator)

## Mục tiêu Kỹ năng

Tạo ra một báo cáo marketing định dạng PDF chuyên nghiệp, được thiết kế đẹp mắt sử dụng file Python hỗ trợ `scripts/generate_pdf_report.py`. Kỹ năng này tổng hợp tất cả dữ liệu audit và phân tích thu thập được, tổ chức thành cấu trúc JSON chuẩn, gọi chạy script Python và xuất ra file PDF mang thương hiệu Bitsness hoàn chỉnh với các biểu đồ gauge điểm số, biểu đồ cột ngang, bảng so sánh đối thủ, các phát hiện chính và kế hoạch hành động ưu tiên.

## Khi nào sử dụng

- Người dùng muốn xuất báo cáo marketing định dạng PDF (thay vì Markdown).
- Người dùng chuẩn bị tài liệu bàn giao chuyên nghiệp để thuyết trình cho khách hàng.
- Người dùng yêu cầu "báo cáo đẹp", "báo cáo gửi khách hàng", hoặc "báo cáo PDF".
- Người dùng muốn có báo cáo trực quan sinh động chứa biểu đồ và điểm số.
- Được kích hoạt bởi lệnh `/market report-pdf` hoặc `/market report-pdf <domain>`.

## Khi nào nên dùng PDF so với Markdown

| Định dạng | Phù hợp nhất cho | Ưu điểm | Nhược điểm |
|---|---|---|---|
| **PDF** | Thuyết trình khách hàng, đính kèm email, tài liệu bán hàng | Giao diện cực kỳ chuyên nghiệp, giữ nguyên định dạng, có biểu đồ trực quan, dễ in ấn | Khó chỉnh sửa nội dung trực tiếp, cần cài đặt môi trường chạy Python |
| **Markdown** | Lưu hành nội bộ, tra cứu nhanh, chỉnh sửa lặp lại, kiểm soát phiên bản (git) | Dễ dàng chỉnh sửa câu chữ, đọc được bằng mọi trình soạn thảo | Tính thẩm mỹ giao diện ở mức cơ bản, không hiển thị biểu đồ động |

**Nguyên tắc chung:** Nếu báo cáo gửi cho khách hàng hoặc đối tác tiềm năng, hãy chọn PDF. Nếu dùng để nghiên cứu nội bộ hoặc cần chỉnh sửa tiếp, hãy chọn Markdown.

## Hướng dẫn thực hiện

### Bước 1: Thu thập tất cả dữ liệu hiện có

Thu thập dữ liệu từ tất cả các lệnh audit đã chạy trước đó. Tìm các file sau trong thư mục dự án:

**Nguồn dữ liệu chính:**
- `MARKETING-AUDIT.md` -- Kết quả audit tổng thể.
- `LANDING-CRO.md` -- Phân tích chuyển đổi Landing Page.
- `SEO-AUDIT.md` -- Phát hiện về SEO.
- `BRAND-VOICE.md` -- Phân tích giọng điệu thương hiệu.
- `COMPETITOR-ANALYSIS.md` -- So sánh đối thủ cạnh tranh.
- `FUNNEL-ANALYSIS.md` -- Phân tích phễu chuyển đổi.
- `SOCIAL-AUDIT.md` -- Audit mạng xã hội.
- `EMAIL-AUDIT.md` -- Audit email marketing.
- `AD-AUDIT.md` -- Audit quảng cáo Ads.

**Nếu chưa có dữ liệu nào trước đó:**
1. Khuyên người dùng nên chạy lệnh `/market audit <url>` trước để có dữ liệu tốt nhất.
2. Nếu người dùng vẫn muốn xuất PDF trực tiếp, hãy phân tích URL trang web được cung cấp và tự xây dựng cấu trúc dữ liệu từ đầu.
3. Chạy script `analyze_page.py` để tự động lấy dữ liệu: `python scripts/analyze_page.py <url>`.

### Bước 2: Xây dựng cấu trúc dữ liệu JSON

Script `scripts/generate_pdf_report.py` yêu cầu dữ liệu đầu vào là 1 file JSON có cấu trúc chính xác sau:

```json
{
  "url": "https://example.com",
  "date": "March 1, 2026",
  "brand_name": "Example Co",
  "overall_score": 62,
  "executive_summary": "Tóm tắt từ 2-4 câu về sức khỏe marketing tổng thể, các cơ hội lớn nhất phát hiện và ước tính doanh thu tăng thêm khi triển khai cải tiến.",
  "categories": {
    "Content & Messaging": {
      "score": 68,
      "weight": "25%"
    },
    "Conversion Optimization": {
      "score": 52,
      "weight": "20%"
    },
    "SEO & Discoverability": {
      "score": 74,
      "weight": "20%"
    },
    "Competitive Positioning": {
      "score": 48,
      "weight": "15%"
    },
    "Brand & Trust": {
      "score": 70,
      "weight": "10%"
    },
    "Growth & Strategy": {
      "score": 55,
      "weight": "10%"
    }
  },
  "findings": [
    {
      "severity": "Critical",
      "finding": "Mô tả phát hiện lỗi nghiêm trọng nhất cần sửa ngay"
    },
    {
      "severity": "High",
      "finding": "Mô tả phát hiện lỗi mức độ ưu tiên cao"
    },
    {
      "severity": "Medium",
      "finding": "Mô tả phát hiện lỗi mức độ ưu tiên trung bình"
    },
    {
      "severity": "Low",
      "finding": "Mô tả phát hiện lỗi nhỏ ưu tiên thấp"
    }
  ],
  "quick_wins": [
    "Đầu việc tối ưu nhanh thứ nhất",
    "Đầu việc tối ưu nhanh thứ hai",
    "Đầu việc tối ưu nhanh thứ ba"
  ],
  "medium_term": [
    "Đầu việc trung hạn thứ nhất",
    "Đầu việc trung hạn thứ hai",
    "Đầu việc trung hạn thứ ba"
  ],
  "strategic": [
    "Đầu việc chiến lược thứ nhất",
    "Đầu việc chiến lược thứ hai",
    "Đầu việc chiến lược thứ ba"
  ],
  "competitors": [
    {
      "name": "Đối thủ A",
      "positioning": "Định vị thị trường của họ",
      "pricing": "Mô hình định giá của họ",
      "social_proof": "Các tín hiệu uy tín của họ",
      "content": "Cách tiếp cận nội dung của họ"
    },
    {
      "name": "Đối thủ B",
      "positioning": "Định vị thị trường của họ",
      "pricing": "Mô hình định giá của họ",
      "social_proof": "Các tín hiệu uy tín của họ",
      "content": "Cách tiếp cận nội dung của họ"
    }
  ]
}
```

### Bước 3: Hướng dẫn chuẩn hóa thông tin dữ liệu

#### `url` (string, bắt buộc)
URL của website phân tích. Điền đầy đủ giao thức (http/https).

#### `date` (string, bắt buộc)
Ngày tạo báo cáo. Khuyên dùng định dạng tiếng Việt: "Ngày DD tháng MM, YYYY" hoặc định dạng chuẩn.

#### `brand_name` (string, bắt buộc)
Tên thương hiệu doanh nghiệp. Dùng làm nhãn hiển thị trong cột bảng so sánh đối thủ.

#### `overall_score` (integer, 0-100, bắt buộc)
Điểm trung bình có trọng số của các danh mục. Công thức tính:
```
overall_score = (content * 0.25) + (conversion * 0.20) + (seo * 0.20) + (competitive * 0.15) + (brand * 0.10) + (growth * 0.10)
```

#### `executive_summary` (string, bắt buộc)
Tóm tắt ngắn gọn từ 2-4 câu bao quát:
- Hiện trạng sức khỏe marketing.
- 1-2 phát hiện lỗi có ảnh hưởng lớn nhất.
- Ước tính tác động doanh thu hàng tháng khi sửa đổi.
- Hành động khuyến nghị đầu tiên cần làm ngay.

Nội dung cần ngắn gọn và cô đọng vì phần này sẽ hiển thị ngay tại trang bìa dưới biểu đồ gauge điểm số.

#### `categories` (object, bắt buộc)
Bắt buộc điền đủ thông số điểm của 6 danh mục chính:

| Danh mục | Nội dung đo lường | Định hướng chấm điểm |
|---|---|---|
| Content & Messaging | Chất lượng copy, Value Proposition, tính rõ ràng của Headline, chữ nút CTA, tính đồng bộ Brand Voice | Điểm 80+: Tiêu đề rõ ràng, hướng lợi ích cụ thể. Điểm 60-79: Đạt yêu cầu nhưng viết chung chung. Điểm <60: Mơ hồ, chỉ nói tính năng |
| Conversion Optimization | Social proof, thiết kế form, vị trí đặt CTA, xử lý phản đối, tính khẩn cấp | Điểm 80+: Có nhiều social proof tốt, form tối ưu, CTA rõ ràng. Điểm 60-79: Có vài yếu tố cơ bản. Điểm <60: Thiếu hụt các thành phần chuyển đổi |
| SEO & Discoverability | Thẻ title, meta description, heading, schema, internal link, tốc độ tải trang | Điểm 80+: Được tối ưu hoàn hảo. Điểm 60-79: Đạt phần lớn nhưng còn vài lỗ hổng. Điểm <60: Gặp lỗi lớn kỹ thuật SEO |
| Competitive Positioning | Sự khác biệt, minh bạch giá, nội dung so sánh đối thủ, độ nhạy thị trường | Điểm 80+: Định vị rõ ràng, có trang so sánh. Điểm 60-79: Có khác biệt nhẹ. Điểm <60: Định vị mờ nhạt |
| Brand & Trust | Chất lượng thiết kế giao diện, trust badges, chứng chỉ bảo mật, tính chuyên nghiệp | Điểm 80+: Thiết kế hiện đại, nhiều tín hiệu uy tín. Điểm 60-79: Thiết kế trung bình. Điểm <60: Giao diện lỗi thời |
| Growth & Strategy | Cơ chế thu thập lead, email marketing, chiến lược content, kênh traffic | Điểm 80+: Có chiến lược đa kênh tốt. Điểm 60-79: Có vài kênh hoạt động. Điểm <60: Chưa có chiến lược tăng trưởng rõ |

#### `findings` (array, bắt buộc)
Mảng chứa các phát hiện lỗi, mỗi phát hiện gồm trường mức độ nghiêm trọng `severity` và mô tả chi tiết `finding`.

**Các mức độ nghiêm trọng (Severity):**
- `Critical` -- Lỗi làm thất thoát trực tiếp doanh thu hoặc khách hàng. Cần sửa ngay.
- `High` -- Ảnh hưởng lớn đến tăng trưởng doanh nghiệp. Cần sửa trong vòng 1-2 tuần.
- `Medium` -- Cơ hội cải tiến tốt. Cần sửa trong vòng 1 tháng.
- `Low` -- Đầu việc tối ưu nhỏ. Sắp xếp sửa khi rảnh.

Đặt mục tiêu từ 5-10 phát hiện lỗi chính. Sắp xếp thứ tự từ lỗi nghiêm trọng nhất xuống thấp dần.

#### `quick_wins` (array, bắt buộc)
3-5 đầu việc tối ưu nhanh làm được ngay trong tuần đầu tiên với nỗ lực tối thiểu. Mỗi đầu việc phải là hướng dẫn hành động cụ thể rõ ràng.

#### `medium_term` (array, bắt buộc)
3-5 đầu việc cải tiến cần từ 1-3 tháng để triển khai. Đây là các đầu việc phức tạp hơn nhưng đem lại hiệu quả cao.

#### `strategic` (array, bắt buộc)
3-5 đầu việc chiến lược cần 3-6 tháng triển khai. Đây là các nâng cấp mang tính hệ thống, nền tảng, đòi hỏi chuẩn bị bài bản.

#### `competitors` (array, tùy chọn)
Tối đa 3 đối thủ cạnh tranh cho bảng so sánh. Nếu không có dữ liệu đối thủ, hãy lược bỏ trường này -- script sẽ tự động bỏ qua phần so sánh đối thủ trong file PDF xuất ra.

### Bước 4: Tạo file JSON tạm thời

Lưu trữ dữ liệu JSON đã thiết lập vào một file tạm:

```bash
# Ghi dữ liệu JSON vào một file tạm thời
cat > /tmp/report_data.json << 'JSONEOF'
{
  ... nội dung file JSON ...
}
JSONEOF
```

### Bước 5: Gọi chạy script Python tạo PDF

**Kiểm tra môi trường thư viện:**
Đảm bảo đã cài đặt thư viện `reportlab`:
```bash
python3 -c "import reportlab" 2>/dev/null || pip3 install reportlab
```

**Chạy lệnh tạo báo cáo:**
```bash
python3 scripts/generate_pdf_report.py /tmp/report_data.json "MARKETING-REPORT-<domain>.pdf"
```

Thay thế cụm `<domain>` bằng tên domain của website phân tích (lược bỏ http/https và www, thay dấu chấm bằng dấu gạch ngang). Ví dụ:
- `example.com` tương ứng đặt tên `MARKETING-REPORT-example-com.pdf`
- `myapp.io` tương ứng đặt tên `MARKETING-REPORT-myapp-io.pdf`

**Chế độ chạy thử nghiệm (Demo mode):**
Chạy script không truyền đối số sẽ tự động sinh ra một file PDF báo cáo mẫu:
```bash
python3 scripts/generate_pdf_report.py
# Sinh ra file: MARKETING-REPORT-sample.pdf
```

### Bước 6: Xác minh kết quả

Sau khi chạy xong lệnh, xác minh file PDF đã được tạo thành công:
```bash
ls -la "MARKETING-REPORT-<domain>.pdf"
```

Thông báo lại đường dẫn và dung lượng file PDF đã xuất cho người dùng biết.

### Bước 7: Dọn dẹp hệ thống

Xóa file JSON tạm thời để tránh rác hệ thống:
```bash
rm /tmp/report_data.json
```

---

## Cấu trúc nội dung báo cáo PDF được tạo ra

File PDF được sinh ra bao gồm các trang sau:

### Trang 1: Trang bìa (Cover Page)
- Tiêu đề báo cáo: "Bitsness Marketing Audit Report" (hoặc tên tùy chỉnh).
- URL trang web phân tích.
- Ngày tạo báo cáo.
- Biểu đồ gauge điểm số tổng thể (vòng tròn màu sắc biểu diễn điểm số).
- Hạng đánh giá (từ A+ đến F).
- Đoạn tóm tắt điều hành (Executive Summary).

### Trang 2: Chi tiết điểm số (Score Breakdown)
- Biểu đồ cột ngang biểu diễn điểm số của cả 6 danh mục chính.
- Bảng chi tiết: danh mục, điểm số, trọng số điểm, trạng thái đánh giá.
- Quy chuẩn màu sắc: Xanh lá (80+), Xanh dương (60-79), Vàng (40-59), Đỏ (<40).

### Trang 3: Các phát hiện chính (Key Findings)
- Bảng tổng hợp các phát hiện lỗi kèm theo nhãn mức độ nghiêm trọng và mô tả chi tiết.
- Nhãn lỗi được tô màu tương ứng: Critical = đỏ, High = cam, Medium = vàng, Low = xanh dương.
- Danh sách xếp hạng từ lỗi nặng nhất xuống lỗi nhẹ hơn.

### Trang 4: Kế hoạch hành động ưu tiên (Action Plan)
- Nhóm Quick Wins (Thực hiện trong tuần đầu).
- Nhóm Trung hạn (Thực hiện trong 1-3 tháng).
- Nhóm Chiến lược (Thực hiện trong 3-6 tháng).
- Các đầu việc được đánh số cụ thể ở mỗi nhóm.

### Trang 5: Bức tranh cạnh tranh (Nếu có dữ liệu đối thủ)
- Bảng so sánh trực quan giữa doanh nghiệp mục tiêu và tối đa 3 đối thủ.
- Các tiêu chí: Định vị thông điệp, Giá cả, Social Proof, Cách làm Content.

### Trang cuối: Phương pháp đánh giá (Methodology)
- Diễn giải phương pháp luận chấm điểm.
- Trọng số điểm và tiêu chí đo lường của từng danh mục.
- Chân trang ghi rõ thương hiệu: "Generated by Bitsness AI Marketing Agent".

---

## Hệ màu sắc chuẩn của Bitsness PDF

Báo cáo PDF sử dụng bảng màu thương hiệu chuyên nghiệp:

| Thành phần hiển thị | Tên màu | Mã Hex |
|---|---|---|
| Primary (tiêu đề, heading) | Dark Navy (Xanh hải quân đậm) | #1B2A4A |
| Accent (đường link, điểm nhấn) | Blue (Xanh dương) | #2D5BFF |
| Highlight (cảnh báo lỗi) | Orange (Cam) | #FF6B35 |
| Success (điểm cao, an toàn) | Green (Xanh lá) | #00C853 |
| Warning (điểm trung bình) | Amber (Vàng hổ phách) | #FFB300 |
| Danger (điểm yếu, critical) | Red (Đỏ) | #FF1744 |
| Light background (màu nền phụ) | Light Gray (Xám nhạt) | #F5F7FA |
| Body text (nội dung chính) | Dark Gray (Xám tối) | #2C3E50 |
| Secondary text (nội dung phụ) | Medium Gray (Xám trung bình) | #7F8C9B |
| Đường viền bảng (Borders) | Light Border (Viền nhạt) | #E0E6ED |

---

## Tích hợp chéo với các kỹ năng khác

Kỹ năng xuất PDF hoạt động tối ưu nhất khi được kết hợp với các bước audit trước đó theo quy trình:

1. Chạy lệnh `/market audit <url>` -- Tạo dữ liệu audit tổng quan.
2. Chạy lệnh `/market competitors <url>` -- Bổ sung dữ liệu so sánh đối thủ.
3. Chạy lệnh `/market seo <url>` -- Bổ sung chi tiết lỗi kỹ thuật SEO.
4. Chạy lệnh `/market landing <url>` -- Bổ sung phân tích chuyển đổi Landing Page.
5. Chạy lệnh `/market report-pdf <url>` -- Tổng hợp và xuất bản file PDF hoàn chỉnh.

Script PDF sẽ tự động tìm kiếm các file kết quả của các lệnh trên trong thư mục để nạp dữ liệu vào file JSON nén trước khi sinh PDF.
