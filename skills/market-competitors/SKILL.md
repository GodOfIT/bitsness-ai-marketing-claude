# Báo cáo Phân tích Thông tin Cạnh tranh về Đối thủ (Competitive Intelligence Analysis)

Bạn là công cụ phân tích thông tin cạnh tranh về đối thủ cho lệnh `/market competitors <url>`. Bạn sẽ xác định các đối thủ cạnh tranh trực tiếp và gián tiếp, phân tích chiến lược marketing của họ, và tạo ra một báo cáo so sánh toàn diện giúp chỉ ra các lỗ hổng định vị trên thị trường, các chiến thuật đáng học hỏi từ đối thủ, và các cơ hội tạo sự khác biệt cho Bitsness. Kết quả đầu ra được thiết kế phù hợp cho cả việc ra quyết định chiến lược lẫn trình bày cho khách hàng.

## Khi Kỹ năng này được Gọi

Người dùng chạy lệnh `/market competitors <url>`. Quét trang web mục tiêu, xác định đối thủ cạnh tranh, phân tích từng đối thủ và tạo file `COMPETITOR-REPORT.md` chứa thông tin phân tích thực tế hành động được.

---

## Giai đoạn 1: Xác định Đối thủ cạnh tranh

### 1.1 Phân loại Đối thủ cạnh tranh

Xác định đối thủ cạnh tranh theo 3 nhóm phân cấp:

| Nhóm đối thủ | Định nghĩa | Cách tìm kiếm | Số lượng |
|----------|-----------|-------------|-------|
| **Direct Competitors** (Trực tiếp) | Cùng sản phẩm, cùng đối tượng khách hàng, cùng thị trường | Tìm kiếm từ khóa danh mục sản phẩm, kiểm tra xem ai đang xếp hạng | 3-5 |
| **Indirect Competitors** (Gián tiếp) | Khác sản phẩm nhưng giải quyết cùng một vấn đề khách hàng | Tìm kiếm vấn đề khách hàng gặp phải, kiểm tra các cách giải quyết thay thế | 2-3 |
| **Aspirational Competitors** (Mơ ước) | Những đơn vị dẫn đầu thị trường mà doanh nghiệp hướng tới | Các thương hiệu lớn đầu ngành, đơn vị kiến tạo danh mục, các hãng nổi tiếng | 1-2 |

### 1.2 Phương pháp Tìm kiếm Đối thủ

Kết hợp nhiều phương pháp để xác định đối thủ cạnh tranh:

**Phương pháp 1: Tìm kiếm dựa trên Từ khóa (Keyword-based)**
- Tìm kiếm các từ khóa chính của trang web mục tiêu.
- Ghi lại các công ty xuất hiện tại trang 1 của kết quả tìm kiếm.
- Tìm kiếm cụm từ: "[danh mục sản phẩm] software/service/tool" hoặc "[danh mục sản phẩm] tốt nhất".
- Tìm kiếm cụm từ: "giải pháp thay thế [target brand]" hoặc "[target brand] alternatives".
- Tìm kiếm cụm từ so sánh: "[target brand] vs".

**Phương pháp 2: Tìm kiếm dựa trên Website (Site-based)**
- Tìm các trang so sánh đối thủ có sẵn trên trang web mục tiêu.
- Kiểm tra các link liên kết dưới chân trang (footer) về các hiệp hội ngành nghề.
- Xem trang tích hợp (integrations) để tìm các công cụ tương tự.
- Kiểm tra nội dung blog xem có nhắc đến đối thủ nào không.

**Phương pháp 3: Tìm kiếm trên các Nền tảng Đánh giá (Reviews)**
- Tìm kiếm danh mục sản phẩm trên G2, Capterra, Trustpilot.
- Ghi lại các đối thủ được đánh giá cao nhất trong cùng danh mục.
- Sử dụng tính năng "So sánh" (Compare) trên các trang review.

**Phương pháp 4: Tìm kiếm trên Mạng xã hội và Cộng đồng**
- Tìm kiếm trên Reddit cụm từ "khuyên dùng [danh mục sản phẩm]" hoặc "[product category] recommendations".
- Kiểm tra Twitter/X về các thảo luận xoay quanh danh mục sản phẩm.
- Xem trên LinkedIn các công ty được theo dõi bởi cùng tệp khách hàng mục tiêu.

### 1.3 Tự động hóa Thu thập Dữ liệu

Sử dụng script Python tại `scripts/competitor_scanner.py` để tự động thu thập dữ liệu khi có thể:

```
python scripts/competitor_scanner.py --url [competitor-url] --output json
```

Script này có khả năng thu thập:
- Nội dung và metadata của trang chủ.
- Dữ liệu trang bảng giá (nếu công khai).
- Số lượng bài viết blog và các chủ đề gần đây.
- Các link mạng xã hội và số lượng người theo dõi (followers).
- Nhận diện hệ thống công nghệ đang sử dụng (technology stack).
- Chỉ số tốc độ tải trang.

Nếu không dùng được script, hãy sử dụng công cụ `WebFetch` để thu thập thủ công các dữ liệu này cho từng đối thủ cạnh tranh.

---

## Giai đoạn 2: Khung Phân tích Đối thủ (Competitor Analysis Framework)

### 2.1 Phân tích Website và Thông điệp (Messaging)

Đối với mỗi đối thủ cạnh tranh, hãy phân tích:

**Thông điệp truyền thông:**
| Yếu tố | Nội dung cần thu thập | Tại sao quan trọng |
|---------|----------------|----------------|
| **Headline** | Nội dung thẻ H1 chính xác | Thể hiện định vị và Value Prop |
| **Subheadline** | Nội dung văn bản bổ trợ | Cho thấy góc tiếp cận thông điệp phụ |
| **Value Proposition** | Lời hứa giá trị cốt lõi | Xác định vùng định vị họ đang sở hữu |
| **Đối tượng mục tiêu** | Người họ đang hướng tới | Cho thấy phân khúc thị trường họ tập trung |
| **Differentiator chính** | Điểm khác biệt cốt lõi | Thể hiện "con hào cạnh tranh" họ tuyên bố |
| **Tone of voice** | Casual/formal/technical | Cho thấy lựa chọn cá tính thương hiệu |
| **Social Proof** | Loại hình và số lượng | Cho thấy chiến lược xây dựng uy tín |

**Bản đồ Định vị (Positioning Map):**
Định vị mỗi đối thủ trên hai trục tọa độ:
- Trục X: Đơn giản (Simplicity) ←→ Mạnh mẽ (Power)
- Trục Y: Giá rẻ (Affordability) ←→ Cao cấp (Premium)

```
BẢN ĐỒ ĐỊNH VỊ
==============
                    PREMIUM (Cao cấp)
                           |
                           |
            [Competitor C] |  [Aspirational]
                           |
   SIMPLE ─────────────────┼───────────────── POWERFUL
  (Đơn giản)               |                 (Mạnh mẽ)
            [Target]       |  [Competitor A]
                           |
                           |
                     BUDGET (Giá rẻ)
```

Điều chỉnh các trục dựa trên những thuộc tính cạnh tranh cốt lõi của ngành cụ thể đó.

### 2.2 So sánh Giá cả

Xây dựng ma trận so sánh giá chi tiết:

```markdown
| Tính năng/Gói dịch vụ | [Target] | Đối thủ A | Đối thủ B | Đối thủ C |
|-------------|----------|-------------|-------------|-------------|
| Gói miễn phí (Free) | Có/Không | Có/Không | Có/Không | Có/Không |
| Giá Starter | $X/tháng | $X/tháng | $X/tháng | $X/tháng |
| Giá Pro | $X/tháng | $X/tháng | $X/tháng | $X/tháng |
| Enterprise | Liên hệ | Liên hệ | $X/tháng | Liên hệ |
| Dùng thử (Free Trial) | X ngày | X ngày | X ngày | X ngày |
| Chiết khấu năm | X% | X% | X% | X% |
| Tính phí theo user | Có/Không | Có/Không | Có/Không | Có/Không |
| Giới hạn sử dụng | [chi tiết] | [chi tiết] | [chi tiết] | [chi tiết] |
```

**Đánh giá Chiến lược Định giá:**
- Giá của Target đang ở mức cao hơn, thấp hơn hay ngang bằng mức trung bình thị trường?
- Bảng giá công khai minh bạch hay ẩn đi (yêu cầu gọi điện cho sales)?
- Mô hình tính phí nào đang được áp dụng (theo user, theo lượng sử dụng, trọn gói, chia gói)?
- Có chiến thuật mỏ neo giá nào được sử dụng trên trang bảng giá không?
- Trang bảng giá có truyền tải giá trị (value) trước khi đưa ra con số giá tiền không?

### 2.3 Ma trận So sánh Tính năng

Xây dựng bảng so sánh tính năng toàn diện:

```markdown
| Danh mục tính năng | Tính năng cụ thể | [Target] | Đối thủ A | Đối thủ B | Đối thủ C |
|-----------------|---------|----------|--------|--------|--------|
| Core (Cốt lõi) | [Tính năng 1] | Có | Có | Một phần | Không |
| Core (Cốt lõi) | [Tính năng 2] | Có | Có | Có | Có |
| Core (Cốt lõi) | [Tính năng 3] | Một phần | Có | Không | Có |
| Advanced (Nâng cao) | [Tính năng 4] | Không | Có | Không | Có |
| Advanced (Nâng cao) | [Tính năng 5] | Có | Không | Có | Không |
| Tích hợp | [Tính năng 6] | Có | Có | Không | Một phần |
| Hỗ trợ khách hàng | [Tính năng 7] | Có | Một phần | Có | Có |
```

Sử dụng các trạng thái: Có (Full), Một phần (Partial), Không (No), hoặc Thử nghiệm (Beta) để phân loại.

Nêu bật:
- Các tính năng mà Target vượt trội hơn (con hào cạnh tranh - competitive moats).
- Các tính năng mà Target còn thiếu (điểm yếu - vulnerability).
- Các tính năng độc quyền duy nhất của một đối thủ (tiềm năng tạo khác biệt).

### 2.4 Phân tích Cạnh tranh SEO

Phân tích khía cạnh SEO của từng đối thủ:

**Chiến lược Nội dung:**
| Chỉ số | [Target] | Đối thủ A | Đối thủ B | Đối thủ C |
|--------|----------|--------|--------|--------|
| Số bài Blog (ước tính) | X | X | X | X |
| Tần suất đăng bài | X/tuần | X/tuần | X/tuần | X/tuần |
| Độ sâu nội dung | Nông/Vừa/Sâu | | | |
| Định dạng nội dung | Blog/Video/Podcast | | | |
| Chủ đề chính | [danh sách] | [danh sách] | [danh sách] | [danh sách] |

**Chiến lược Từ khóa:**
- Các đối thủ cạnh tranh đang nhắm mục tiêu rõ rệt vào những từ khóa nào?
- Những từ khóa nào mà nhiều đối thủ xếp hạng cao nhưng Target lại vắng bóng? (SEO content gaps)
- Đối thủ có đang viết nội dung so sánh/giải pháp thay thế không?
- Các từ khóa đuôi dài (long-tail keywords) nào đang đem lại traffic cho đối thủ?

**Phân tích Khoảng trống Nội dung (Content Gap Analysis):**
Liệt kê các chủ đề đối thủ viết rất tốt nhưng Target chưa có nội dung:
```
KHOẢNG TRỐNG NỘI DUNG (Content Gaps):
  1. [Chủ đề] — Đối thủ A, B viết tốt (search intent cao)
  2. [Chủ đề] — Đối thủ A, C viết tốt (search intent vừa)
  3. [Chủ đề] — Đối thủ B viết tốt (search intent cao)
  4. [Chủ đề] — Tất cả đối thủ đều viết tốt (lỗ hổng nghiêm trọng cần lấp đầy)
```

### 2.5 So sánh Sự hiện diện trên Mạng xã hội

| Nền tảng | [Target] | Đối thủ A | Đối thủ B | Đối thủ C |
|----------|----------|--------|--------|--------|
| Followers LinkedIn | X | X | X | X |
| Followers Twitter/X | X | X | X | X |
| Followers Instagram | X | X | X | X |
| Subscribers YouTube | X | X | X | X |
| Followers TikTok | X | X | X | X |
| Tần suất đăng bài | X/tuần | X/tuần | X/tuần | X/tuần |
| Tỷ lệ tương tác | X% | X% | X% | X% |
| Định dạng tốt nhất | [loại hình] | [loại hình] | [loại hình] | [loại hình] |

### 2.6 Khai thác Review của khách hàng (Review Mining)

Phân tích ý kiến đánh giá của khách hàng trên các nền tảng bên thứ ba (G2, Capterra, Trustpilot, Reddit):

**Đối với từng đối thủ, hãy trích xuất:**
- Điểm đánh giá trung bình (số sao).
- Số lượng review.
- Top 3 tính năng được khen ngợi nhất (điều khách hàng yêu thích).
- Top 3 lời phàn nàn nhiều nhất (nỗi thất vọng của khách hàng).
- Các lý do phổ biến khi chuyển đổi công cụ (vì sao khách hàng rời bỏ họ).
- Mô hình sử dụng (use cases) được nhắc đến nhiều nhất.

**Ma trận Thông tin Đánh giá (Review Intelligence Matrix):**
```markdown
| Đối thủ cạnh tranh | Điểm số | Số lượng review | Điểm được khen nhiều nhất | Phàn nàn phổ biến | Lý do khách bỏ đi |
|-----------|--------|---------|-----------|---------------|--------------|
| Đối thủ A | 4.5/5 | 500+ | Dễ sử dụng | Tích hợp hạn chế | Tăng giá bán |
| Đối thủ B | 4.2/5 | 200+ | Tính năng mạnh mẽ | Khó làm quen | Support chậm |
| Đối thủ C | 3.8/5 | 100+ | Chi phí hợp lý | Nhiều lỗi vặt | Có giải pháp tốt hơn |
```

---

## Giai đoạn 3: Phân tích SWOT

### 3.1 Phân tích SWOT của từng Đối thủ

Tạo bảng SWOT chi tiết cho từng đối thủ cạnh tranh:

```
ĐỐI THỦ: [Tên đối thủ]
URL: [url]

STRENGTHS (Điểm mạnh):
  - [Điểm mạnh cụ thể kèm bằng chứng]
  - [Điểm mạnh cụ thể kèm bằng chứng]

WEAKNESSES (Điểm yếu):
  - [Điểm yếu cụ thể kèm bằng chứng]
  - [Điểm yếu cụ thể kèm bằng chứng]

OPPORTUNITIES (Cơ hội cho Target khai thác):
  - [Cơ hội dựa trên điểm yếu của đối thủ]
  - [Cơ hội dựa trên khoảng trống thị trường]

THREATS (Mối đe dọa từ đối thủ cần lưu ý):
  - [Mối đe dọa với tác động tiềm tàng]
  - [Mối đe dọa với tác động tiềm tàng]
```

### 3.2 SWOT Tổng hợp của Target

Tổng hợp tất cả các thông tin cạnh tranh thu thập được thành một bảng phân tích SWOT duy nhất cho trang web mục tiêu (Target):

- **Điểm mạnh (Strengths):** Những điểm Target làm tốt hơn tất cả hoặc phần lớn đối thủ.
- **Điểm yếu (Weaknesses):** Những điểm Target đang bị tụt lại phía sau đối thủ.
- **Cơ hội (Opportunities):** Khoảng trống trên thị trường chưa có đối thủ nào giải quyết tốt.
- **Thách thức (Threats):** Những khía cạnh đối thủ đang tỏ ra vượt trội rõ rệt.

---

## Giai đoạn 4: Đề xuất Chiến lược hành động

### 4.1 Các chiến thuật đáng học hỏi ("Steal-Worthy" Tactics)

Xác định các chiến thuật marketing cụ thể của đối thủ mang lại hiệu quả cao mà Target nên học tập áp dụng:

```
CÁC CHIẾN THUẬT ĐÁNG HỌC HỎI
===========================

1. [Đối thủ A] — [Tactic: ví dụ: "Bộ công cụ tính toán ROI trực quan"]
   Tại sao hiệu quả: [giải thích lý do]
   Cách triển khai: [các bước thực hiện cụ thể cho Target]
   Nỗ lực thực hiện: [Thấp/Trung bình/Cao]
   Tác động dự kiến: [Thấp/Trung bình/Cao]

2. [Đối thủ B] — [Tactic: ví dụ: "Chuỗi video case study kể chuyện khách hàng thực tế"]
   Tại sao hiệu quả: [giải thích]
   Cách triển khai: [các bước cụ thể]
   Nỗ lực thực hiện: [Thấp/Trung bình/Cao]
   Tác động dự kiến: [Thấp/Trung bình/Cao]
```

Tập trung vào các chiến thuật:
- Đã được chứng minh hiệu quả (đang chạy tốt cho đối thủ).
- Có khả năng tùy biến (có thể chỉnh sửa phù hợp cho Target).
- Chưa được khai thác sâu (Target hiện tại chưa làm điều này).

### 4.2 Chiến lược Tạo Khác biệt Thông điệp (Messaging Differentiation)

Dựa trên phân tích cạnh tranh, đề xuất cách Target tạo sự khác biệt về thông điệp:

**Khung Tạo Khác Biệt (Differentiation Framework):**
1. **Category (Danh mục):** Target có thể tạo ra hoặc sở hữu một danh mục phụ mới không? (ví dụ: "[thuộc tính cụ thể] [danh mục chính]")
2. **Audience (Đối tượng):** Target có thể nhắm đến một tệp khách hàng chuyên biệt mà đối thủ bỏ qua không?
3. **Feature (Tính năng):** Có tính năng độc đáo nào đối thủ không có mà Target sở hữu không?
4. **Philosophy (Triết lý):** Khác biệt về giá trị cốt lõi, cách tiếp cận hay phương pháp luận giải quyết vấn đề?
5. **Experience (Trải nghiệm):** Khác biệt về dịch vụ chăm sóc khách hàng, hỗ trợ 24/7 hay cộng đồng thành viên?

Với mỗi góc độ tạo khác biệt khả thi, hãy cung cấp:
- Câu tuyên bố định vị (Positioning statement)
- Đề xuất câu Headline tiêu đề tương ứng
- Các bằng chứng/luận điểm bổ trợ (proof points)
- Cách thể hiện cụ thể trên giao diện website

### 4.3 Chiến lược Xây dựng Trang Đối đầu (Alternative Pages)

Đề xuất xây dựng các trang so sánh dạng "[Đối thủ] Alternative":

**Với mỗi đối thủ lớn, phác thảo cấu trúc trang:**
```
TÊN TRANG: [Target Brand] vs [Tên đối thủ]
URL đề xuất: /vs/[ten-doi-thu] hoặc /alternatives/[ten-doi-thu]

Headline: "Bạn đang tìm giải pháp thay thế [Tên đối thủ]? Đây là lý do vì sao nhiều đội nhóm chuyển sang chọn [Target]."

Các phần nội dung chính:
  1. Bảng so sánh nhanh (tính năng, giá cả, đánh giá của người dùng)
  2. Điểm [Target] vượt trội (3-4 lợi thế kèm theo bằng chứng cụ thể)
  3. Điểm [Đối thủ] vượt trội (đánh giá khách quan để tạo lòng tin)
  4. [Target] phù hợp nhất cho ai (mô tả chân dung khách hàng lý tưởng)
  5. Câu chuyện chuyển đổi thực tế (testimonial của khách hàng đã chuyển sang dùng)
  6. Hướng dẫn di chuyển dữ liệu hoặc ưu đãi đặc quyền cho người chuyển đổi
  7. FAQ các câu hỏi thường gặp khi chuyển đổi công cụ
  8. CTA: "Thử [Target] miễn phí" hoặc "Xem so sánh chi tiết"
```

**Giá trị SEO:** Các trang này nhắm trực tiếp vào các từ khóa có ý định mua hàng rất cao ở đáy phễu như "giải pháp thay thế [đối thủ]" hoặc "[target] vs [đối thủ]".

### 4.4 Kịch bản Chuyển đổi Khách hàng (Switching Narratives)

Xây dựng kịch bản truyền thông thuyết phục khách hàng đang dùng đối thủ chuyển sang dùng Target:

```
KỊCH BẢN CHUYỂN ĐỔI: [Đối thủ] → [Target]

Các lý do chính khách hàng rời bỏ đối thủ:
  1. [Lý do hàng đầu dựa trên khai thác review]
  2. [Lý do thứ hai]
  3. [Lý do thứ ba]

Mẫu câu chuyện chuyển đổi (Switching story template):
  "Giống như nhiều [audience], [tên khách hàng] ban đầu lựa chọn [Đối thủ] vì [sức hút ban đầu]. Nhưng sau [thời gian/sự kiện], họ nhận ra [pain point]. Sau khi chuyển sang sử dụng [Target], họ đã đạt được [kết quả cụ thể bằng con số]."

Ưu đãi kích thích chuyển đổi:
  - Hỗ trợ di chuyển dữ liệu miễn phí.
  - Tặng thêm thời gian dùng thử cho người dùng đang dùng đối thủ.
  - Chính sách giá ưu đãi hoặc giảm giá bù đắp chi phí hủy hợp đồng cũ.
  - Quy trình hướng dẫn (onboarding) chuyên biệt cho người chuyển đổi.
```

---

## Giai đoạn 5: Theo dõi và Cập nhật Thông tin Liên tục

### 5.1 Checklist Theo dõi Cạnh tranh

Khuyến nghị các hoạt động theo dõi đối thủ định kỳ:

- [ ] Thiết lập Google Alerts cho tên của từng đối thủ cạnh tranh.
- [ ] Theo dõi các đối thủ trên các nền tảng mạng xã hội chính.
- [ ] Đăng ký nhận bản tin email (newsletter) của đối thủ.
- [ ] Kiểm tra trang bảng giá của đối thủ hàng tháng.
- [ ] Theo dõi các trang review đối thủ hàng quý.
- [ ] Theo dõi tần suất và chủ đề xuất bản nội dung của đối thủ.
- [ ] Chú ý các đợt ra mắt sản phẩm mới hoặc cập nhật tính năng lớn của đối thủ.
- [ ] Theo dõi tin tuyển dụng của đối thủ (tiết lộ định hướng ưu tiên chiến lược của họ).
- [ ] Theo dõi ngân sách quảng cáo và mẫu quảng cáo sáng tạo của đối thủ (sử dụng Meta Ad Library, Google Ads Transparency).
- [ ] Kiểm tra hồ sơ liên kết (backlink profile) của đối thủ hàng quý.

### 5.2 Kịch bản Ứng phó Cạnh tranh (Competitive Response Playbook)

Định hướng cách phản ứng nhanh trước các động thái của đối thủ:

| Động thái của đối thủ | Chiến lược ứng phó | Khung thời gian |
|----------------|-------------------|----------|
| Đối thủ hạ giá bán | Nhấn mạnh vào giá trị và chất lượng sản phẩm, tuyệt đối tránh cuộc chiến dìm giá | 1 tuần |
| Ra mắt tính năng mới | Đánh giá mức độ liên quan thực tế, truyền thông lộ trình phát triển (roadmap) cho khách hàng | 2 tuần |
| Chạy ads rầm rộ | Tập trung tối đa vào các kênh tự sở hữu (owned channels) và giữ chân khách hàng cũ | Liên tục |
| Viết bài so sánh dìm hàng | Tạo nội dung so sánh khách quan, dựa trên dữ liệu thực tế để đối chứng | 1 tuần |
| Được đầu tư lớn / mua lại | Trấn an khách hàng, nhấn mạnh tính ổn định và sự tập trung của thương hiệu | 1-2 ngày |
| Nhận phàn nàn từ khách hàng | Theo dõi sát sao cơ hội tiếp cận, giải quyết các nỗi đau chung mà đối thủ gặp phải | Liên tục |

---

## Định dạng Đầu ra: COMPETITOR-REPORT.md

Lưu báo cáo hoàn chỉnh vào file `COMPETITOR-REPORT.md`:

```markdown
# Báo cáo Thông tin Đối thủ Cạnh tranh: [Tên thương hiệu]
**URL:** [url]
**Ngày thực hiện:** [ngày tháng hiện tại]
**Số lượng đối thủ phân tích:** [số lượng]
**Vị thế cạnh tranh: [Mạnh/Vừa/Yếu]**

---

## Tóm tắt Điều hành (Executive Summary)
[Đoạn tóm tắt từ 3-4 đoạn bao quát bức tranh toàn cảnh cạnh tranh, vị thế hiện tại của Target, điểm mạnh cạnh tranh lớn nhất, mối đe dọa cạnh tranh lớn nhất và top 3 khuyến nghị chiến lược hàng đầu.]

---

## Tổng quan về các Đối thủ cạnh tranh

### Đối thủ Trực tiếp (Direct Competitors)
[Bảng tổng hợp gồm: Tên, URL, Định vị thông điệp, Giá cả, Điểm khác biệt chính]

### Đối thủ Gián tiếp (Indirect Competitors)
[Bảng tổng hợp]

### Đối thủ Mơ ước (Aspirational Competitors)
[Bảng tổng hợp]

---

## Hồ sơ Chi tiết từng Đối thủ

### [Tên Đối thủ A]
[Phân tích đầy đủ: Thông điệp truyền thông, Giá cả, Tính năng, SWOT, Sự hiện diện MXH, Đánh giá của khách hàng]

### [Tên Đối thủ B]
[Phân tích đầy đủ]

[Lặp lại cho từng đối thủ]

---

## Các bảng So sánh trực quan

### So sánh Tính năng (Feature Comparison)
[Ma trận so sánh tính năng đầy đủ]

### So sánh Giá cả (Pricing Comparison)
[Ma trận so sánh giá đầy đủ]

### So sánh Điểm đánh giá (Review Ratings)
[Bảng tổng hợp điểm review G2/Trustpilot]

### Sự hiện diện trên Mạng xã hội
[Bảng so sánh các kênh MXH]

---

## Bản đồ Định vị (Positioning Map)
[Bản đồ định vị dạng text-based kèm theo giải thích chi tiết]

---

## Phân tích Khoảng trống Nội dung & SEO
[Các khoảng trống nội dung blog, cơ hội từ khóa, chiến lược trang so sánh]

---

## Phân tích SWOT Tổng hợp — [Tên thương hiệu]
[Bảng SWOT tổng hợp dựa trên toàn bộ thông tin cạnh tranh thu thập được]

---

## Khuyến nghị Chiến lược hành động

### Các chiến thuật đáng học hỏi (Steal-Worthy Tactics)
[5-10 chiến thuật cụ thể kèm hướng dẫn áp dụng]

### Chiến lược Tạo Khác biệt (Differentiation Strategy)
[Các góc độ và thông điệp định vị khuyên dùng]

### Các trang So sánh Đối thủ cần xây dựng (Alternative Pages)
[Phác thảo cấu trúc các trang so sánh trực diện]

### Kịch bản Chuyển đổi Khách hàng (Switching Narratives)
[Câu chuyện kể và các gói ưu đãi kích thích chuyển đổi cho từng đối thủ chính]

---

## Kế hoạch Theo dõi Cạnh tranh
[Checklist theo dõi định kỳ và kịch bản ứng phó trước các động thái của đối thủ]

---

## Các bước tiếp theo cần làm
1. [Hành động cạnh tranh khẩn cấp nhất]
2. [Hành động ưu tiên thứ hai]
3. [Hành động ưu tiên thứ ba]
```

---

## Định dạng hiển thị ở Terminal

```
=== BẢO CÁO THÔNG TIN ĐỐI THỦ CẠNH TRANH BITSNESS ===

Trang mục tiêu: [name]
Số đối thủ đã phân tích: [count]
Vị thế cạnh tranh: [Mạnh/Vừa/Yếu]

Bức tranh cạnh tranh:
  Trực tiếp:   [Comp A] (Rating: X/5), [Comp B] (Rating: X/5)
  Gián tiếp:   [Comp C], [Comp D]
  Mơ ước:      [Comp E]

Phát hiện cốt lõi:
  Lợi thế lớn nhất: [lợi thế]
  Mối đe dọa lớn nhất: [đe dọa]
  Cơ hội lớn nhất: [cơ hội]

Lỗ hổng tính năng: [X] tính năng đối thủ có nhưng target chưa có
Lỗ hổng nội dung: [X] chủ đề đối thủ viết nhưng target chưa viết
Định vị giá: [Cao hơn/Bằng/Thấp hơn] trung bình thị trường

Top 3 Hành động Cần làm ngay:
  1. [hành động]
  2. [hành động]
  3. [hành động]

Báo cáo đầy đủ đã được lưu vào file: COMPETITOR-REPORT.md
```

---

## Tích hợp chéo giữa các kỹ năng

- Nếu file `MARKETING-AUDIT.md` đã có sẵn, hãy đối chiếu điểm số định vị cạnh tranh trong đó.
- Nếu file `COPY-SUGGESTIONS.md` đã có sẵn, hãy sử dụng thông tin định vị để viết lại thông điệp khác biệt.
- Nếu file `FUNNEL-ANALYSIS.md` đã có sẵn, hãy so sánh hiệu quả phễu chuyển đổi của bạn với đối thủ.
- Nếu file `AD-CAMPAIGNS.md` đã có sẵn, hãy áp dụng thông tin đối thủ để viết quảng cáo so sánh.
- Gợi ý các lệnh tiếp theo: chạy lệnh `/market copy` để tối ưu thông điệp khác biệt, chạy lệnh `/market ads` để triển khai chiến dịch quảng cáo đối đầu, chạy lệnh `/market funnel` để tối ưu phễu chuyển đổi.
