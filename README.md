<p align="center">
  <img src="resources/logo.jpg" alt="Bitsness AI Marketing Suite" width="100%">
</p>

# Bitsness AI Marketing Suite cho Claude Code

Hệ thống skill tự động hóa và phân tích marketing toàn diện dành cho [Claude Code](https://docs.anthropic.com/en/docs/claude-code). Kiểm tra marketing của bất kỳ website nào, tạo nội dung copy, xây dựng chuỗi email marketing, lên lịch nội dung mạng xã hội, phân tích đối thủ cạnh tranh và xuất báo cáo PDF chuyên nghiệp gửi cho khách hàng — tất cả ngay từ terminal của bạn.

**Được thiết kế cho các doanh nghiệp, agency marketing và các solopreneur muốn cung cấp dịch vụ marketing chất lượng cao được tăng cường bởi AI.**

---

## Tính năng nổi bật

Gõ câu lệnh trong Claude Code và nhận kết quả phân tích marketing hành động được ngay lập tức:

```
> /market audit https://calendly.com

Đang khởi chạy 5 sub-agent chạy song song...
✓ Phân tích Content & Messaging     — Điểm: 72/100
✓ Tối ưu hóa Conversion (CRO)       — Điểm: 58/100
✓ Phân tích SEO & Discoverability   — Điểm: 81/100
✓ Định vị Cạnh tranh (Competitors)   — Điểm: 64/100
✓ Thương hiệu & Độ tin cậy (Trust)   — Điểm: 76/100
✓ Chiến lược Tăng trưởng (Growth)    — Điểm: 61/100

Điểm Marketing tổng thể: 69/100

Báo cáo đầy đủ đã được lưu vào file MARKETING-AUDIT.md
```

---

## Hướng dẫn cài đặt

### Cài đặt nhanh bằng 1 câu lệnh

```bash
curl -fsSL https://raw.githubusercontent.com/GodOfIT/bitsness-ai-marketing-claude/main/install.sh | bash
```

### Cài đặt thủ công

```bash
git clone https://github.com/GodOfIT/bitsness-ai-marketing-claude.git
cd bitsness-ai-marketing-claude
./install.sh
```

### Yêu cầu tùy chọn: Xuất báo cáo PDF

```bash
pip install reportlab
```

---

## Danh sách câu lệnh chính

| Câu lệnh | Chức năng |
|---------|-------------|
| `/market audit <url>` | Kiểm tra marketing toàn diện với 5 sub-agent chạy song song |
| `/market quick <url>` | Nhận bản chụp nhanh (snapshot) marketing trong 60 giây |
| `/market copy <url>` | Tạo nội dung copy được tối ưu kèm theo ví dụ Before/After |
| `/market emails <chủ đề>` | Tạo chuỗi email marketing hoàn chỉnh |
| `/market social <chủ đề>` | Lên kế hoạch lịch nội dung mạng xã hội trong 30 ngày |
| `/market ads <url>` | Viết nội dung và ý tưởng quảng cáo Ads cho các nền tảng |
| `/market funnel <url>` | Phân tích và tối ưu hóa phễu bán hàng (Sales Funnel) |
| `/market competitors <url>` | Tạo báo cáo thông tin cạnh tranh về đối thủ |
| `/market landing <url>` | Phân tích tối ưu hóa chuyển đổi Landing Page (CRO) |
| `/market launch <sản phẩm>` | Lên kế hoạch chi tiết (playbook) ra mắt sản phẩm |
| `/market proposal <khách hàng>` | Tạo đề xuất dịch vụ (client proposal) gửi cho khách hàng |
| `/market report <url>` | Tạo báo cáo marketing định dạng Markdown |
| `/market report-pdf <url>` | Tạo báo cáo marketing PDF chuyên nghiệp cho khách hàng |
| `/market seo <url>` | Kiểm tra SEO và chất lượng nội dung |
| `/market brand <url>` | Phân tích tính cách và bộ nguyên tắc giọng điệu thương hiệu |

---

## Kiến trúc thư mục

```
bitsness-ai-marketing-claude/
├── market/SKILL.md                     # Điều phối chính (định tuyến các lệnh /market)
│
├── skills/                             # 14 kỹ năng phụ (sub-skills)
│   ├── market-audit/SKILL.md           # Điều phối toàn bộ quá trình audit
│   ├── market-copy/SKILL.md            # Phân tích & tạo nội dung copy
│   ├── market-emails/SKILL.md          # Tạo chuỗi email marketing
│   ├── market-social/SKILL.md          # Lên lịch nội dung mạng xã hội
│   ├── market-ads/SKILL.md             # Viết nội dung quảng cáo Ads
│   ├── market-funnel/SKILL.md          # Phân tích & tối ưu hóa phễu
│   ├── market-competitors/SKILL.md     # Báo cáo thông tin đối thủ cạnh tranh
│   ├── market-landing/SKILL.md         # Phân tích tối ưu hóa Landing Page
│   ├── market-launch/SKILL.md          # Kế hoạch playbook ra mắt sản phẩm
│   ├── market-proposal/SKILL.md        # Biểu mẫu đề xuất dịch vụ
│   ├── market-report/SKILL.md          # Báo cáo marketing (Markdown)
│   ├── market-report-pdf/SKILL.md      # Báo cáo marketing (PDF)
│   ├── market-seo/SKILL.md             # Phân tích và audit SEO
│   └── market-brand/SKILL.md           # Phân tích giọng điệu thương hiệu
│
├── agents/                             # 5 sub-agent chạy song song
│   ├── market-content.md               # Phân tích Content & Messaging
│   ├── market-conversion.md            # Tối ưu hóa CRO & phễu
│   ├── market-competitive.md           # Định vị và phân tích đối thủ cạnh tranh
│   ├── market-technical.md             # Đánh giá kỹ thuật SEO & tracking
│   └── market-strategy.md              # Chiến lược giá, thương hiệu & tăng trưởng
│
├── scripts/                            # Các file mã nguồn Python bổ trợ
│   ├── analyze_page.py                 # Phân tích webpage tự động
│   ├── competitor_scanner.py           # Quét website đối thủ cạnh tranh
│   ├── social_calendar.py              # Tạo lịch nội dung mạng xã hội
│   └── generate_pdf_report.py          # Script xuất file báo cáo PDF
│
├── templates/                          # Các biểu mẫu marketing mẫu
│   ├── email-welcome.md                # Chuỗi email chào mừng (5 email)
│   ├── email-nurture.md                # Chuỗi email nuôi dưỡng (6 email)
│   ├── email-launch.md                 # Chuỗi email ra mắt sản phẩm (8 email)
│   ├── proposal-template.md            # Mẫu đề xuất gửi khách hàng
│   ├── content-calendar.md             # Lịch nội dung mẫu trong 30 ngày
│   └── launch-checklist.md             # Checklist ra mắt sản phẩm
│
├── logo.jpg                            # Ảnh logo Bitsness đại diện
├── install.sh                          # Script cài đặt nhanh
├── uninstall.sh                        # Script gỡ cài đặt sạch sẽ
├── requirements.txt                    # Các thư viện Python phụ thuộc
└── LICENSE                             # Giấy phép MIT License
```

---

## Phương pháp chấm điểm (Scoring Methodology)

Kiểm tra marketing toàn diện đánh giá website trên 6 khía cạnh chính:

| Danh mục | Trọng số | Nội dung đánh giá |
|----------|--------|------------------|
| Content & Messaging | 25% | Chất lượng copy, Value Proposition, tính rõ ràng, sức thuyết phục |
| Conversion Optimization | 20% | Thiết kế CTA, form, social proof, giảm ma sát, tạo tính cấp bách |
| SEO & Discoverability | 20% | On-page SEO, Technical SEO, cấu trúc nội dung |
| Competitive Positioning | 15% | Sự khác biệt, định vị giá, trang so sánh đối thủ cạnh tranh |
| Brand & Trust | 10% | Chất lượng thiết kế, các tín hiệu uy tín, bằng chứng xã hội |
| Growth & Strategy | 10% | Chiến lược định giá, kênh thu hút, cơ hội giới thiệu/giữ chân |

**Điểm Marketing tổng thể** = Trung bình có trọng số của cả 6 danh mục đánh giá (0-100)

---

## Nguyên lý hoạt động

1. **Nhập câu lệnh** — Ví dụ: `/market audit https://example.com`
2. **Claude đọc file kỹ năng** — Hướng dẫn chi tiết cách đánh giá website.
3. **5 sub-agent chạy song song** — Mỗi agent phân tích một khía cạnh riêng biệt.
4. **Chạy các file Python** — Tự động phân tích trang và quét đối thủ.
5. **Tổng hợp kết quả** — Tạo báo cáo có chấm điểm kèm danh sách hành động ưu tiên.
6. **Lưu kết quả** — Lưu dưới dạng Markdown hoặc PDF chuyên nghiệp.

---

## Bản quyền

Giấy phép MIT License — xem [LICENSE](LICENSE) để biết thêm chi tiết.
