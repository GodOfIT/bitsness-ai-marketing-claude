# Phân tích Brand Voice và Thiết lập Bộ nguyên tắc Giọng điệu

## Mục tiêu Kỹ năng

Phân tích Brand Voice, tone giọng và thông điệp truyền thông của thương hiệu trên tất cả các kênh hiện có, từ đó tạo ra một tài liệu bộ nguyên tắc (guidelines) chi tiết về Brand Voice. Kỹ năng này kiểm tra cách thương hiệu giao tiếp, xác định các điểm đặc trưng hoặc sự thiếu nhất quán, và xuất ra bộ nguyên tắc hành động được để bất kỳ copywriter hay marketer nào cũng có thể theo sát nhằm duy trì tính đồng bộ của thương hiệu.

## Khi nào sử dụng

- Người dùng muốn hiểu rõ hoặc ghi chép lại tài liệu Brand Voice của thương hiệu.
- Người dùng cần một bộ Brand Voice Guidelines gửi cho đội ngũ, freelancer hoặc agency.
- Người dùng muốn đảm bảo tính đồng bộ thông điệp trên mọi kênh marketing.
- Doanh nghiệp đang tái định vị (rebranding) hoặc tinh chỉnh nhận diện thương hiệu.
- Người dùng muốn so sánh Brand Voice của mình với các đối thủ cạnh tranh.
- Được kích hoạt bởi lệnh `/market brand <url>` hoặc `/market brand`.

## Cách thực hiện

### Bước 1: Thu thập tài liệu nguồn

Để phân tích Brand Voice, hãy kiểm tra nội dung từ nhiều nguồn khác nhau theo thứ tự ưu tiên sau:

**Nguồn sơ cấp (Bắt buộc phân tích):**
1. **Trang chủ (Homepage)** -- Nơi thể hiện rõ nhất cách sắp xếp thông điệp thương hiệu.
2. **Trang giới thiệu (About page)** -- Cách thương hiệu tự mô tả về mình.
3. **Trang sản phẩm/dịch vụ** -- Cách thương hiệu trình bày các giải pháp cung cấp.

**Nguồn thứ cấp (Phân tích nếu có sẵn):**
4. **Các bài viết Blog** (tối thiểu 3-5 bài viết gần nhất).
5. **Hồ sơ mạng xã hội (Social media)** (phần tiểu sử bio, các bài đăng gần đây, phong cách tương tác).
6. **Bản tin Email (Newsletters)** (email chào mừng welcome email, các email gửi gần đây).
7. **Nội dung tương tác khách hàng (UX copy)** (thông báo lỗi, luồng onboarding, tài liệu hỗ trợ).

**Nguồn tam cấp:**
8. **Tin tuyển dụng** -- Tiết lộ văn hóa nội bộ và các giá trị cốt lõi.
9. **Thông cáo báo chí (Press releases)** -- Phong cách giao tiếp trang trọng.
10. **Nội dung quảng cáo (Ad copy)** -- Cách tiếp cận thông điệp trả phí.
11. **Kịch bản video hoặc podcast** -- Giọng nói thương hiệu ở dạng hội thoại nói.

Sử dụng các công cụ trình duyệt hoặc script `analyze_page.py` để lấy nội dung web. Đối với mạng xã hội, kiểm tra các link liên kết trên website và phân tích các trang hồ sơ được trỏ tới.

### Bước 2: Phân tích 4 chiều của Brand Voice

Định vị Brand Voice của thương hiệu theo 4 khía cạnh chính. Mỗi khía cạnh là một dải quang phổ (spectrum) từ mức độ này sang mức độ khác, không phải nhị phân.

#### Khía cạnh 1: Formal (Trang trọng) <-----> Casual (Thân mật)

Thương hiệu nằm ở đâu trên dải quang phổ trang trọng?

| Dấu hiệu | Formal | Casual |
|---|---|---|
| Từ viết tắt | Tránh dùng | Sử dụng tự do thoải mái |
| Cấu trúc câu | Phức tạp, câu dài, chỉn chu | Ngắn gọn, súc tích, đi thẳng vào vấn đề |
| Từ vựng | Chuyên nghiệp, đúng chuẩn ngành | Dễ hiểu, như văn nói giao tiếp hàng ngày |
| Lời chào | "Kính gửi quý khách hàng" | "Xin chào bạn!" |
| Đại từ xưng hô | Ngôi thứ ba ("công ty", "chúng tôi") | Ngôi thứ nhất/thứ hai ("mình", "bạn", "ta") |
| Yếu tố hài hước | Rất hiếm hoặc không có | Xuất hiện thường xuyên, tự nhiên |
| Tiếng lóng/khẩu ngữ | Không bao giờ | Đôi khi hoặc thường xuyên |

**Điểm số: từ 1 (Formal cực kỳ) đến 10 (Casual cực kỳ)**

**Yêu cầu bằng chứng:** Trích dẫn cụ thể 3-5 ví dụ từ tài liệu nguồn để minh chứng cho điểm số đánh giá.

#### Khía cạnh 2: Serious (Nghiêm túc) <-----> Playful (Vui vẻ)

Mức độ vui vẻ, hài hước được đưa vào giao tiếp như thế nào?

| Dấu hiệu | Serious | Playful |
|---|---|---|
| Tone giọng | Uy tín, chừng mực | Nhẹ nhàng, vui tươi, năng động |
| Phép ẩn dụ | Hiếm, chừng mực | Sáng tạo, bất ngờ, độc đáo |
| Dấu chấm than | Hiếm khi dùng | Sử dụng thường xuyên |
| Sử dụng Emoji | Không bao giờ | Thỉnh thoảng hoặc rất thường xuyên |
| Chơi chữ/từ lóng | Không bao giờ | Ưa thích và hay sử dụng |
| Thông báo lỗi | "Đã xảy ra lỗi hệ thống" | "Ối! Có gì đó sai sai rồi" |
| Tự trào (Self-deprecation) | Không bao giờ | Thỉnh thoảng xuất hiện |

**Điểm số: từ 1 (Serious cực kỳ) đến 10 (Playful cực kỳ)**

#### Khía cạnh 3: Technical (Kỹ thuật) <-----> Simple (Đơn giản)

Thương hiệu giả định mức độ chuyên môn của đối tượng độc giả ở mức nào?

| Dấu hiệu | Technical | Simple |
|---|---|---|
| Thuật ngữ (Jargon) | Sử dụng tự do các thuật ngữ chuyên ngành | Tránh dùng hoặc giải thích cặn kẽ |
| Từ viết tắt | Dùng trực tiếp không cần giải thích | Giải nghĩa đầy đủ ở lần dùng đầu tiên |
| Mức độ chi tiết | Giải thích sâu về kỹ thuật/vận hành | Tóm tắt khái quát ở mức vĩ mô |
| Giả định độc giả | Độc giả là chuyên gia trong ngành | Độc giả là người dùng phổ thông |
| Số liệu/thống kê | Chi tiết, tần suất xuất hiện cao | Thỉnh thoảng, được đơn giản hóa trực quan |
| Ví dụ minh họa | Phức tạp, đặc thù chuyên môn | Các phép so sánh đơn giản, gần gũi |

**Điểm số: từ 1 (Technical cực kỳ) đến 10 (Simple cực kỳ)**

#### Khía cạnh 4: Reserved (Kín đáo) <-----> Bold (Táo bạo)

Thương hiệu thể hiện cá tính và sự tự tin mạnh mẽ đến mức nào?

| Dấu hiệu | Reserved | Bold |
|---|---|---|
| Tuyên bố | Thận trọng ("chúng tôi tin", "có thể giúp") | Trực diện ("cam kết", "tốt nhất", "hàng đầu") |
| Quan điểm | Trung lập, cân bằng | Mạnh mẽ, rõ ràng, có chính kiến |
| Nhắc tới đối thủ | Tránh nhắc tới đối thủ cạnh tranh | So sánh trực diện |
| Cá tính | Chuyên nghiệp, nhã nhặn, chừng mực | Nổi bật, cá tính, dễ nhớ |
| Lời hứa | Thận trọng, thực tế | Tham vọng, đột phá |
| Chủ đề tranh cãi | Tuyệt đối tránh | Sẵn sàng thảo luận nếu khớp với giá trị cốt lõi |

**Điểm số: từ 1 (Reserved cực kỳ) đến 10 (Bold cực kỳ)**

### Bước 3: Định hình Tone Spectrum

Ngoài 4 khía cạnh trên, hãy vẽ sơ đồ cách tone giọng của thương hiệu thay đổi theo từng bối cảnh cụ thể:

| Bối cảnh | Tone giọng điển hình | Ví dụ cụ thể |
|---|---|---|
| Trang chủ | [Tự tin/Chào đón/Khẩn cấp/v.v.] | "[trích dẫn từ trang chủ]" |
| Mô tả sản phẩm | [Thông tin/Thuyết phục/Kỹ thuật/v.v.] | "[trích dẫn]" |
| Bài viết Blog | [Giáo dục/Giao tiếp/Uy tín/v.v.] | "[trích dẫn]" |
| Mạng xã hội | [Casual/Tương tác/Quảng bá/v.v.] | "[trích dẫn]" |
| Trang báo lỗi/404 | [Xin lỗi/Hài hước/Hỗ trợ/v.v.] | "[trích dẫn]" |
| Tiêu đề Email | [Trực diện/Tò mò/Khẩn cấp/v.v.] | "[trích dẫn]" |
| Nút CTA | [Hướng hành động/Hướng lợi ích/Khẩn cấp/v.v.] | "[trích dẫn]" |
| Hỗ trợ khách hàng | [Thấu cảm/Chuyên nghiệp/Thân thiện/v.v.] | "[trích dẫn]" |

### Bước 4: Khung cá tính thương hiệu (Brand Personality Framework)

Khớp thương hiệu vào một trong 5 hình mẫu cá tính cốt lõi (archetypes) (có thể kết hợp từ 1-2 hình mẫu):

#### 5 Hình mẫu cốt lõi

**1. The Authority (Nhà cầm quyền/Chuyên gia)**
- Đặc điểm: Chuyên gia, đáng tin cậy, dựa trên số liệu, có vị thế.
- Giọng điệu: Tự tin nhưng không kiêu ngạo, mang tính giáo dục, chính xác.
- Ngành phù hợp: Tài chính, y tế, B2B enterprise, luật, tư vấn doanh nghiệp.
- Thương hiệu ví dụ: McKinsey, IBM, Mayo Clinic.
- Cụm từ hay dùng: "Nghiên cứu chỉ ra...", "Chuyên gia của chúng tôi...", "Dẫn đầu ngành..."

**2. The Innovator (Nhà đổi mới/Khai phóng)**
- Đặc điểm: Tiên phong, đột phá, tầm nhìn xa, am hiểu công nghệ.
- Giọng điệu: Hào hứng, hướng về tương lai, đôi khi khiêu khích thử thách giới hạn.
- Ngành phù hợp: Công nghệ, SaaS, startup, năng lượng tái tạo.
- Thương hiệu ví dụ: Tesla, Stripe, Notion.
- Cụm từ hay dùng: "Tái định nghĩa...", "Tương lai của...", "Chúng tôi đang xây dựng..."

**3. The Friend (Người bạn đồng hành)**
- Đặc điểm: Ấm áp, dễ tiếp cận, hữu ích, gần gũi.
- Giọng điệu: Giao tiếp, thấu cảm, cởi mở, khuyến khích.
- Ngành phù hợp: Sản phẩm tiêu dùng, giáo dục, nền tảng cộng đồng.
- Thương hiệu ví dụ: Mailchimp, Slack, Duolingo.
- Cụm từ hay dùng: "Chúng tôi hiểu rằng...", "Bạn làm được mà...", "Sẵn sàng hỗ trợ bạn..."

**4. The Rebel (Kẻ nổi loạn/Khác biệt)**
- Đặc điểm: Táo bạo, thách thức các quy chuẩn, cá tính mạnh, nhiệt huyết.
- Giọng điệu: Trực diện, có chính kiến rõ ràng, ấn tượng sâu sắc.
- Ngành phù hợp: Phong cách sống, thể thao, ngành sáng tạo, D2C.
- Thương hiệu ví dụ: Nike, Oatly, Cards Against Humanity.
- Cụm từ hay dùng: "Ngừng chấp nhận...", "Sự thật là...", "Chúng tôi đã chán ngấy với..."

**5. The Guide (Người dẫn đường)**
- Đặc điểm: Sáng suốt, kiên nhẫn, bài bản, đáng tin cậy.
- Giọng điệu: Rõ ràng, hướng dẫn chi tiết, hỗ trợ tận tình, hiểu biết sâu rộng.
- Ngành phù hợp: Giáo dục, phát triển kỹ năng chuyên môn, công cụ, nền tảng.
- Thương hiệu ví dụ: HubSpot, Khan Academy, Ahrefs.
- Cụm từ hay dùng: "Đây là cách để...", "Từng bước một...", "Hướng dẫn toàn tập về..."

**Đánh giá:**
- Archetype chính: [loại hình mẫu và lý do chọn]
- Archetype phụ: [nếu có]
- Mức độ phù hợp: [Mạnh/Vừa/Yếu -- mức độ thương hiệu thể hiện hình mẫu này]

### Bước 5: Phân tích vốn từ vựng (Vocabulary Analysis)

Xác định các quy luật chọn từ ngữ của thương hiệu:

#### Nhóm từ thường dùng
Phân tích tất cả tài liệu nguồn và xác định 15-20 từ/cụm từ đặc trưng nhất. Tổ chức theo danh mục:

**Từ ngữ hành động (Động từ ưa thích):**
- Ví dụ: "xây dựng", "tăng quy mô (scale)", "chuyển đổi", "tối giản hóa (streamline)"

**Từ ngữ mô tả (Tính từ hay dùng):**
- Ví dụ: "mạnh mẽ", "đơn giản", "chuẩn doanh nghiệp (enterprise-grade)", "dễ dàng"

**Từ ngữ giá trị (Từ thể hiện giá trị cốt lõi):**
- Ví dụ: "minh bạch", "bền vững", "bao trùm (inclusive)", "đổi mới sáng tạo"

**Thuật ngữ chuyên ngành:**
- Ví dụ: "quy trình (workflow)", "phễu (pipeline)", "chuyển đổi (conversion)", "tương tác (engagement)"

#### Nhóm từ cần tránh
Xác định những từ ngữ hoàn toàn vắng bóng hoặc không phù hợp với cá tính thương hiệu:
- Từ ngữ quá thân mật (nếu thương hiệu thuộc dạng Formal).
- Từ ngữ quá chuyên môn kỹ thuật (nếu thương hiệu thuộc dạng Simple).
- Thuật ngữ của đối thủ cạnh tranh mà thương hiệu chủ ý tránh dùng.
- Các sáo rỗng (cliches) trong ngành mà thương hiệu né tránh.

#### Cụm từ mang chữ ký (Signature Phrases)
Thương hiệu có cụm từ lặp lại, slogan hay thói quen sử dụng ngôn ngữ đặc trưng nào không?
- Slogan/Tagline: [nếu có]
- Cụm từ lặp lại: [quy luật phát hiện được]
- Thói quen ngôn ngữ: [ví dụ: luôn bắt đầu câu bằng động từ, hay dùng dấu gạch ngang, chuộng viết đoạn văn ngắn]

### Bước 6: So sánh Brand Voice với đối thủ cạnh tranh

So sánh Brand Voice của thương hiệu với 2-3 đối thủ cạnh tranh chính:

**Ma trận so sánh (Voice Comparison Matrix):**
| Khía cạnh | [Thương hiệu của bạn] | Đối thủ 1 | Đối thủ 2 | Đối thủ 3 |
|---|---|---|---|---|
| Formal <> Casual | X/10 | X/10 | X/10 | X/10 |
| Serious <> Playful | X/10 | X/10 | X/10 | X/10 |
| Technical <> Simple | X/10 | X/10 | X/10 | X/10 |
| Reserved <> Bold | X/10 | X/10 | X/10 | X/10 |
| Archetype chính | [hình mẫu] | [hình mẫu] | [hình mẫu] | [hình mẫu] |

**Đánh giá khác biệt (Differentiation Assessment):**
- Brand Voice của thương hiệu khác biệt như thế nào so với đối thủ?
- Các thương hiệu có điểm giao thoa giọng điệu nào không? (cơ hội để tạo sự khác biệt)
- Vùng không gian giọng điệu nào còn đang bỏ trống trên thị trường?
- Các khuyến nghị cụ thể để tạo sự khác biệt về Brand Voice.

### Bước 7: Kiểm tra tính đồng bộ (Consistency Audit)

Đánh giá mức độ đồng bộ của Brand Voice trên tất cả các kênh được phân tích:

| Kênh truyền thông | Mức độ đồng bộ | Ghi chú chi tiết |
|---|---|---|
| Trang chủ | Đồng bộ/Phần lớn/Không đồng bộ | [quan sát cụ thể] |
| Trang giới thiệu | Đồng bộ/Phần lớn/Không đồng bộ | [ghi chú] |
| Blog | Đồng bộ/Phần lớn/Không đồng bộ | [ghi chú] |
| Mạng xã hội | Đồng bộ/Phần lớn/Không đồng bộ | [ghi chú] |
| Email | Đồng bộ/Phần lớn/Không đồng bộ | [ghi chú] |
| Trang sản phẩm | Đồng bộ/Phần lớn/Không đồng bộ | [ghi chú] |

**Các vấn đề mất đồng bộ phổ biến:**
- Nhiều người viết khác nhau tạo ra các tone giọng khác biệt rõ rệt.
- Giọng điệu trên MXH khác biệt quá xa so với trên website.
- Nội dung website rất trang trọng nhưng bản tin email lại quá thân mật.
- Nội dung Blog viết theo tone giọng hoàn toàn khác với các trang giới thiệu sản phẩm.
- Các thông báo lỗi hoặc UX copy tạo cảm giác lạc quẻ, không đúng thương hiệu.
- Các trang cũ chưa được cập nhật theo định hướng Brand Voice mới.

**Điểm đồng bộ tổng thể:** X/10

### Bước 8: Hệ thống cấp bậc thông điệp (Brand Messaging Hierarchy)

Ghi chép lại thông điệp thương hiệu từ mức độ tóm gọn nhất đến chi tiết nhất:

#### Cấp độ 1: Tagline (Dưới 10 từ)
Dạng cô đọng nhất của thông điệp thương hiệu.
- Hiện tại: "[tagline đang có hoặc đề xuất mới]"
- Đánh giá: Có lột tả được Value Proposition cốt lõi không?

#### Cấp độ 2: Value Propositions (1 câu cho mỗi ý)
3-5 Value Proposition cốt lõi bổ trợ cho lời hứa thương hiệu.
1. "[Value prop 1]"
2. "[Value prop 2]"
3. "[Value prop 3]"

#### Cấp độ 3: Elevator Pitch (Bài thuyết trình ngắn - 30 giây / 75 từ)
Cách giải thích tự nhiên về việc thương hiệu làm gì và tại sao nó lại quan trọng.
"[Bản nháp Elevator Pitch dựa trên nội dung đã phân tích]"

#### Cấp độ 4: Boilerplate (Mô tả chuẩn - 100-150 từ)
Đoạn giới thiệu "về chúng tôi" tiêu chuẩn dùng trong thông cáo báo chí, chữ ký email hay hồ sơ diễn giả.
"[Bản nháp Boilerplate dựa trên nội dung đã phân tích]"

#### Cấp độ 5: Câu chuyện thương hiệu đầy đủ (Full Brand Story - 300-500 từ)
Bản tự sự hoàn chỉnh về việc thương hiệu là ai, đại diện cho điều gì và tại sao lại tồn tại trên thị trường.
- Trạng thái hiện tại: [Đã có/Một phần/Chưa có]
- Khuyến nghị cải thiện.

### Bước 9: Tạo tài liệu Brand Voice Guidelines (Do's and Don'ts)

Xây dựng bộ hướng dẫn chi tiết những việc NÊN và KHÔNG NÊN làm:

#### Bảng đối chiếu giọng điệu (Voice Chart)

```
GIỌNG ĐIỆU CỦA CHÚNG TA LÀ:           GIỌNG ĐIỆU CỦA CHÚNG TA KHÔNG PHẢI LÀ:
-------------------------------------------------------------------------
[Đặc tính 1]                        [Đặc tính phản diện 1]
Ví dụ: "Tự tin"                     Ví dụ: "Kiêu ngạo"

[Đặc tính 2]                        [Đặc tính phản diện 2]
Ví dụ: "Hữu ích"                    Ví dụ: "Ban ơn/Cửa trên"

[Đặc tính 3]                        [Đặc tính phản diện 3]
Ví dụ: "Rõ ràng"                    Ví dụ: "Hời hợt/Trẻ con"

[Đặc tính 4]                        [Đặc tính phản diện 4]
Ví dụ: "Táo bạo"                    Ví dụ: "Gây hấn/Thô lỗ"
```

#### Quy tắc NÊN và KHÔNG NÊN khi viết

**NÊN (DO):**
- [Hướng dẫn viết cụ thể dựa trên phân tích]
- [Ví dụ: "Sử dụng các câu ngắn, chủ động để giữ nhịp độ đọc nhanh"]
- [Ví dụ: "Đưa lợi ích trực tiếp lên đầu trước khi nói về tính năng"]
- [Ví dụ: "Luôn dùng ngôi thứ hai xưng hô trực tiếp với người đọc như 'bạn', 'của bạn'"]

**KHÔNG NÊN (DON'T):**
- [Các lỗi hành văn cần tránh dựa trên phân tích]
- [Ví dụ: "Không dùng thuật ngữ kỹ thuật phức tạp mà không có giải thích đi kèm"]
- [Ví dụ: "Tránh dùng câu bị động trong các lời kêu gọi hành động CTA"]
- [Ví dụ: "Không lạm dụng dấu chấm than quá nhiều lần trong một đoạn văn"]

### Bước 10: Mẫu viết thử nghiệm (Copy Samples)

Cung cấp 5-8 đoạn copy mẫu viết chuẩn theo Brand Voice đã định hình để đội ngũ tham chiếu trực tiếp:

**1. Tiêu đề Trang chủ (Homepage Headline):**
"[Đoạn mẫu]"

**2. Mô tả sản phẩm (Product Description):**
"[Đoạn mẫu]"

**3. Mở đầu bài viết Blog (Blog Post Opening):**
"[Đoạn mẫu]"

**4. Bài đăng Mạng xã hội (Social Media Post):**
"[Đoạn mẫu]"

**5. Tiêu đề Email (Email Subject Line):**
"[Đoạn mẫu]"

**6. Nội dung nút kêu gọi (CTA Button Text):**
"[Đoạn mẫu]"

**7. Thông báo lỗi (Error Message):**
"[Đoạn mẫu]"

**8. Lời cảm ơn khách hàng (Customer Thank You):**
"[Đoạn mẫu]"

## Định dạng Đầu ra: BRAND-VOICE.md

Tạo file có tên `BRAND-VOICE.md` trong thư mục hiện tại với cấu trúc:

```markdown
# Bộ nguyên tắc Giọng điệu Thương hiệu (Brand Voice Guidelines)
## [Tên thương hiệu]
### Ngày thực hiện phân tích: [Ngày tháng]

---

## Tóm tắt Giọng điệu (Voice Summary)
[Tóm tắt dài 2-3 câu về Brand Voice, cá tính và các đặc trưng giao tiếp nổi bật của thương hiệu]

---

## Khía cạnh Giọng điệu (Voice Dimensions)

### Formal (Trang trọng) <-----> Casual (Thân mật): [X/10]
[Bằng chứng và diễn giải chi tiết]

### Serious (Nghiêm túc) <-----> Playful (Vui vẻ): [X/10]
[Bằng chứng và diễn giải chi tiết]

### Technical (Kỹ thuật) <-----> Simple (Đơn giản): [X/10]
[Bằng chứng và diễn giải chi tiết]

### Reserved (Kín đáo) <-----> Bold (Táo bạo): [X/10]
[Bằng chứng và diễn giải chi tiết]

### Bản đồ Giọng điệu Trực quan (Visual Voice Map)
```
Formal                                    Casual
|----[X]----------------------------------|
Serious                                   Playful
|--------[X]------------------------------|
Technical                                 Simple
|------------------[X]--------------------|
Reserved                                  Bold
|------------[X]--------------------------|
```

---

## Cá tính Thương hiệu (Brand Personality)
- Archetype chính: [Tên hình mẫu]
- Archetype phụ: [Tên hình mẫu]
- [Diễn giải chi tiết kèm bằng chứng]

---

## Tone giọng theo bối cảnh
| Bối cảnh | Tone giọng | Ví dụ thực tế |
|---|---|---|
| [bối cảnh] | [tone] | "[ví dụ]" |

---

## Vốn từ vựng đặc trưng

### Từ ngữ khuyên dùng (Words We Use)
[Các từ vựng được phân loại cụ thể]

### Từ ngữ cần tránh (Words We Avoid)
[Các từ không phù hợp với cá tính thương hiệu]

### Cụm từ mang chữ ký (Signature Phrases)
[Các cụm từ đặc trưng, thói quen ngôn ngữ lặp lại]

---

## Bảng đối chiếu giọng điệu (Voice Chart)
| Giọng điệu của chúng ta LÀ | Giọng điệu của chúng ta KHÔNG PHẢI LÀ |
|---|---|
| [trait] | [anti-trait] |

---

## Nguyên tắc viết nội dung (Writing Guidelines)

### Nên làm (Do's)
- [nguyên tắc cụ thể]

### Không nên làm (Don'ts)
- [lỗi cần tránh]

---

## Hệ thống cấp bậc thông điệp (Brand Messaging Hierarchy)

### Tagline
[slogan/tagline]

### Value Propositions (Các tuyên bố giá trị)
1. [tuyên bố 1]

### Elevator Pitch
[bài giới thiệu ngắn]

### Boilerplate (Giới thiệu chuẩn)
[giới thiệu boilerplate]

---

## Các đoạn mẫu chuẩn (Copy Samples)
[8 ví dụ copy viết chuẩn theo Brand Voice]

---

## So sánh giọng điệu với đối thủ cạnh tranh
[Ma trận so sánh đối thủ và phân tích tạo điểm khác biệt]

---

## Đánh giá tính đồng bộ (Consistency Audit)
[Đánh giá chi tiết theo từng kênh truyền thông]
- Điểm đồng bộ tổng thể: [X/10]

---

## Đề xuất hành động tiếp theo
### Hành động tức thì
1. [đề xuất 1]

### Cơ hội phát triển giọng điệu
1. [đề xuất 1]

### Cải thiện tính nhất quán
1. [đề xuất 1]
```

## Các nguyên tắc cốt lõi

- Phân tích Brand Voice đòi hỏi sự tỉ mỉ như một thám tử. Mọi cách lựa chọn từ ngữ, dấu câu hay cấu trúc câu đều tiết lộ cách thương hiệu muốn được nhìn nhận trên thị trường.
- Luôn đưa ra BẰNG CHỨNG cho mỗi đánh giá. Đừng chỉ kết luận "thương hiệu này thân mật" -- hãy trích dẫn các ví dụ thực tế trên web chứng minh điều đó.
- Bộ nguyên tắc Brand Voice phải đủ rõ ràng để một người mới tinh có thể đọc hiểu và viết đúng ngay từ bài viết đầu tiên.
- Các đoạn viết mẫu (copy samples) là phần có giá trị thực tiễn nhất. Người viết học giọng điệu nhanh nhất qua ví dụ thực tế chứ không phải qua mô tả lý thuyết. Hãy đa dạng hóa các đoạn mẫu.
- Voice (Giọng điệu) và Tone (Giọng thế) là khác nhau. Voice là cá tính đồng nhất xuyên suốt. Tone thay đổi linh hoạt theo ngữ cảnh giao tiếp (trả lời khiếu nại khách hàng sẽ có tone khác với email thông báo ra mắt sản phẩm mới, nhưng cả hai đều chung một Voice).
- Nếu phát hiện thấy sự mất nhất quán về giọng điệu giữa các kênh, hãy trình bày điều đó như một cơ hội cải thiện để nâng tầm thương hiệu Bitsness của họ, thay vì đánh giá đó là một lỗi sai nghiêm trọng.
- Nếu người dùng đã chạy lệnh `/market competitors` trước đó, hãy sử dụng lại dữ liệu đó cho phần so sánh giọng điệu đối thủ.
