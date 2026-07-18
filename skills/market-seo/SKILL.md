# Kiểm tra & Tối ưu hóa SEO (SEO Content Audit)

## Mục tiêu Kỹ năng

Thực hiện audit SEO toàn diện cho một trang web hoặc toàn bộ website, bao gồm các mảng: On-page SEO, đánh giá chất lượng nội dung theo chuẩn E-E-A-T, phân tích từ khóa (keyword), đánh giá kỹ thuật SEO (Technical SEO) và đề xuất chiến lược phát triển nội dung. Kỹ năng này kết hợp chạy script phân tích tự động `scripts/analyze_page.py` với đánh giá chuyên sâu để xuất ra tài liệu audit SEO thực tế hành động được.

## Khi nào sử dụng

- Người dùng cung cấp URL và yêu cầu phân tích SEO, audit hoặc đưa ra khuyến nghị cải thiện.
- Người dùng muốn cải thiện thứ hạng tìm kiếm tự nhiên (organic search) và tăng lượng traffic.
- Người dùng hỏi về tối ưu hóa On-page SEO, các thẻ meta, chất lượng nội dung hay kỹ thuật SEO.
- Người dùng muốn phân tích khoảng trống nội dung (content gap) hoặc lên chiến lược content mới.
- Được kích hoạt bởi lệnh `/market seo <url>` hoặc `/market seo`.

## Hướng dẫn thực hiện

### Bước 1: Chạy Script Phân tích Tự động

Sử dụng script Python để thu thập dữ liệu kỹ thuật SEO nền tảng:

```bash
python3 scripts/analyze_page.py <url>
```

Script này tự động trích xuất:
- Thẻ Title và Meta Description.
- Các thẻ Open Graph phục vụ chia sẻ MXH.
- Cấu trúc tiêu đề (thẻ H1-H6).
- Danh sách các liên kết (internal và external links).
- Danh sách hình ảnh và trạng thái thẻ Alt text.
- Các biểu mẫu form và nút CTA.
- Dữ liệu cấu trúc Schema.
- Các link tài khoản mạng xã hội.
- Các script theo dõi tracking được cài đặt.
- Thẻ Viewport meta (chỉ số thân thiện di động).
- Thẻ Canonical.
- Các chỉ thị Robots meta.

Lấy kết quả JSON đầu ra làm cơ sở dữ liệu để thực hiện bước phân tích chuyên sâu tiếp theo.

### Bước 2: Checklist kiểm tra On-Page SEO

Đánh giá từng yếu tố và xếp hạng theo các mức: Đạt (Pass), Cần tối ưu (Needs Work), hoặc Chưa đạt (Fail).

#### Thẻ Title (Tiêu đề trang)
| Tiêu chí | Tiêu chuẩn tối ưu | Đánh giá |
|---|---|---|
| Có tồn tại | Mỗi trang phải có một thẻ Title độc nhất | Đạt/Chưa đạt |
| Độ dài | Từ 50-60 ký tự (để hiển thị đầy đủ trên SERPs, không bị cắt dấu ba chấm) | Đạt/Cần tối ưu/Chưa đạt |
| Từ khóa chính | Chứa từ khóa mục tiêu chính của trang | Đạt/Cần tối ưu/Chưa đạt |
| Vị trí từ khóa | Từ khóa chính nên được đặt ở phần đầu của thẻ Title | Đạt/Cần tối ưu/Chưa đạt |
| Tên thương hiệu | Có chứa tên thương hiệu (đặt ở cuối thẻ, ngăn cách bởi dấu gạch | hoặc -) | Đạt/Cần tối ưu/Chưa đạt |
| Tính độc nhất | Khác biệt so với thẻ Title của các trang khác trên cùng website | Đạt/Chưa đạt |
| Độ cuốn hút | Có đủ hấp dẫn kích thích người tìm kiếm nhấp vào không? | Đạt/Cần tối ưu/Chưa đạt |

**Các lỗi thẻ Title phổ biến:**
- Quá dài (bị cắt cụt trên trang kết quả tìm kiếm).
- Thiếu từ khóa chính.
- Nhồi nhét từ khóa (ví dụ: "Phần mềm SEO tốt nhất | Công cụ SEO hàng đầu | SEO Tool | SEO Platform").
- Dùng chung một Title cho nhiều trang khác nhau.
- Viết quá chung chung ("Trang chủ", "Chào mừng", "Trang 1").
- Thiếu tên thương hiệu Bitsness ở cuối.

#### Thẻ Meta Description (Mô tả trang)
| Tiêu chí | Tiêu chuẩn tối ưu | Đánh giá |
|---|---|---|
| Có tồn tại | Mọi trang quan trọng đều nên có Meta Description | Đạt/Chưa đạt |
| Độ dài | Từ 150-160 ký tự | Đạt/Cần tối ưu/Chưa đạt |
| Từ khóa chính | Chèn từ khóa chính một cách tự nhiên | Đạt/Cần tối ưu/Chưa đạt |
| Lời kêu gọi hành động | Chứa lý do hấp dẫn thúc đẩy người dùng click | Đạt/Cần tối ưu/Chưa đạt |
| Tính độc nhất | Khác biệt so với các trang khác trên web | Đạt/Chưa đạt |
| Độ cuốn hút | Đóng vai trò như một đoạn quảng cáo ngắn cho kết quả tìm kiếm | Đạt/Cần tối ưu/Chưa đạt |

#### Cấu trúc tiêu đề (Heading H1-H6)
| Tiêu chí | Tiêu chuẩn tối ưu | Đánh giá |
|---|---|---|
| Có thẻ H1 | Mỗi trang chỉ được phép có duy nhất một thẻ H1 | Đạt/Chưa đạt |
| H1 chứa từ khóa | Chèn từ khóa chính vào thẻ H1 | Đạt/Cần tối ưu/Chưa đạt |
| H1 khác thẻ Title | Thẻ H1 và thẻ Title nên viết khác nhau (nhưng đồng bộ nội dung) | Đạt/Cần tối ưu/Chưa đạt |
| Phân cấp logic | Thẻ H2 nằm dưới H1, H3 dưới H2 (tuyệt đối không nhảy cóc cấp độ) | Đạt/Cần tối ưu/Chưa đạt |
| Tiêu đề phụ rõ nghĩa | Các thẻ H2, H3 mô tả đúng nội dung của phần đó | Đạt/Cần tối ưu/Chưa đạt |
| Từ khóa trong H2/H3 | Chèn từ khóa phụ một cách tự nhiên vào H2, H3 | Đạt/Cần tối ưu/Chưa đạt |
| Không lạm dụng | Dùng thẻ Heading để phân cấu trúc nội dung, không dùng để định dạng font | Đạt/Cần tối ưu/Chưa đạt |

#### Tối ưu hóa Hình ảnh (Image Optimization)
| Tiêu chí | Tiêu chuẩn tối ưu | Đánh giá |
|---|---|---|
| Thẻ Alt text | Tất cả hình ảnh minh họa đều phải có thẻ Alt text | Đạt/Cần tối ưu/Chưa đạt |
| Chất lượng Alt | Alt mô tả đúng nội dung ảnh và chèn từ khóa tự nhiên | Đạt/Cần tối ưu/Chưa đạt |
| Tên file ảnh | Đặt tên file mô tả hình ảnh (ví dụ: thiet-ke-web-bitsness.jpg, tránh IMG_001.jpg) | Đạt/Cần tối ưu/Chưa đạt |
| Dung lượng ảnh | Được tối ưu dung lượng (ưu tiên định dạng WebP, đã nén ảnh) | Đạt/Cần tối ưu/Chưa đạt |
| Lazy loading | Các hình ảnh nằm dưới nếp gấp màn hình được bật chế độ lazy loading | Đạt/Cần tối ưu/Chưa đạt |
| Ảnh responsive | Sử dụng srcset hoặc thẻ picture cho các kích thước màn hình khác nhau | Đạt/Cần tối ưu/Chưa đạt |
| Ảnh trang trí | Các ảnh chỉ dùng trang trí set Alt trống alt="" (tránh thiếu thuộc tính alt) | Đạt/Chưa đạt |

#### Liên kết nội bộ (Internal Linking)
| Tiêu chí | Tiêu chuẩn tối ưu | Đánh giá |
|---|---|---|
| Có internal links | Trang có liên kết trỏ tới các nội dung liên quan khác trên cùng web | Đạt/Cần tối ưu/Chưa đạt |
| Chữ neo (Anchor text) | Chữ hiển thị chứa từ khóa mô tả trang trỏ tới (tránh viết "bấm vào đây") | Đạt/Cần tối ưu/Chưa đạt |
| Liên kết sâu | Trỏ đến các bài viết, dịch vụ cụ thể sâu hơn (tránh chỉ trỏ về trang chủ) | Đạt/Cần tối ưu/Chưa đạt |
| Ngữ cảnh liên quan | Link được chèn tự nhiên, khớp ngữ cảnh nội dung xung quanh | Đạt/Cần tối ưu/Chưa đạt |
| Số lượng hợp lý | Khoảng 3-10 link nội bộ cho mỗi 1,000 từ nội dung | Đạt/Cần tối ưu/Chưa đạt |
| Link lỗi (Broken link) | Không có internal link nào bị lỗi 404 | Đạt/Chưa đạt |

#### Cấu trúc URL
| Tiêu chí | Tiêu chuẩn tối ưu | Đánh giá |
|---|---|---|
| Dễ đọc | URL thân thiện với người dùng, mô tả đúng nội dung | Đạt/Cần tối ưu/Chưa đạt |
| Chứa từ khóa | URL có chứa từ khóa chính không dấu | Đạt/Cần tối ưu/Chưa đạt |
| Độ dài | Ngắn gọn, dưới 75 ký tự (tối ưu nhất là dưới 60) | Đạt/Cần tối ưu/Chưa đạt |
| Dấu gạch ngang | Ngăn cách các từ bằng dấu gạch ngang - (tránh dùng dấu gạch dưới _) | Đạt/Chưa đạt |
| Chữ viết thường | Viết thường toàn bộ ký tự | Đạt/Chưa đạt |
| Không chứa tham số | URL sạch, không chứa các query parameter rườm rà | Đạt/Cần tối ưu/Chưa đạt |
| Dấu gạch chéo cuối | Đồng bộ cấu trúc URL (luôn có hoặc không bao giờ có dấu / ở cuối) | Đạt/Cần tối ưu/Chưa đạt |

### Bước 3: Đánh giá chất lượng nội dung theo chuẩn E-E-A-T

Đánh giá chất lượng nội dung trang web dựa trên bộ khung E-E-A-T của Google:

#### Experience (Trải nghiệm thực tế)
Nội dung có chứng minh được tác giả là người đã có trải nghiệm thực tế với chủ đề đó không?

**Dấu hiệu nhận biết:**
- Có chia sẻ câu chuyện cá nhân, case study cụ thể hoặc ví dụ thực tế.
- Có ảnh chụp màn hình, ảnh tự quay chụp, minh chứng trải nghiệm thực tế.
- Các chi tiết chuyên sâu mà chỉ người đã trải nghiệm thực tế mới biết.
- Nội dung dạng "Tôi đã tự làm X và đây là kết quả thực tế đạt được".

**Đánh giá:** Mạnh (Strong) / Đạt (Present) / Yếu (Weak) / Chưa có (Missing)

#### Expertise (Tính chuyên môn)
Người viết có chuyên môn sâu rộng về chủ đề này không?

**Dấu hiệu nhận biết:**
- Có thông tin tác giả (bio) ghi rõ chứng chỉ, kinh nghiệm chuyên môn liên quan.
- Bài viết có độ sâu kiến thức (không viết nông cạn hời hợt).
- Cung cấp thông tin và dữ liệu chính xác, khoa học.
- Sử dụng chuẩn xác thuật ngữ chuyên ngành.
- Có link trỏ tới nguồn dẫn số liệu uy tín bên ngoài.

**Đánh giá:** Mạnh / Đạt / Yếu / Chưa có

#### Authoritativeness (Tính thẩm quyền/Uy tín)
Website và tác giả có được công nhận là một uy tín lớn trong mảng này không?

**Dấu hiệu nhận biết:**
- Có thông tin tên tuổi, ảnh đại diện thật của tác giả.
- Trang giới thiệu cung cấp rõ ràng bối cảnh và quy mô công ty.
- Đạt được các giải thưởng hoặc chứng chỉ chuyên môn của ngành.
- Có backlinks từ các trang web uy tín lớn trỏ về.
- Có tin tức báo chí chính thống nhắc tới.
- Tác giả có các bài viết guest post trên các trang tạp chí lớn của ngành.

**Đánh giá:** Mạnh / Đạt / Yếu / Chưa có

#### Trustworthiness (Độ tin cậy)
Độc giả có thể tuyệt đối tin tưởng nội dung và website này không?

**Dấu hiệu nhận biết:**
- Trang web cài đặt bảo mật HTTPS (chứng chỉ SSL).
- Có trang Chính sách bảo mật và Điều khoản dịch vụ rõ ràng.
- Hiển thị rõ địa chỉ thực tế và thông tin liên hệ của doanh nghiệp.
- Có hiển thị review và testimonial của khách hàng.
- Có các chứng nhận bảo mật thanh toán.
- Thông tin minh bạch, chính xác và được cập nhật mới thường xuyên.
- Có trích dẫn rõ nguồn gốc của các số liệu thống kê sử dụng trong bài.

**Đánh giá:** Mạnh / Đạt / Yếu / Chưa có

### Bước 4: Phân tích Từ khóa (Keyword Analysis)

#### Đánh giá Từ khóa chính
| Thành phần | Tiêu chí phân tích |
|---|---|
| Xác định từ khóa chính | Từ khóa mục tiêu trang này đang muốn nhắm tới là gì? |
| Khớp ý định tìm kiếm (Search Intent) | Nội dung trang có đáp ứng đúng kỳ vọng của người tìm kiếm từ khóa đó không? (Dạng tìm kiếm thông tin informational, thương mại commercial, giao dịch transactional, hay điều hướng navigational) |
| Từ khóa trong thẻ Title | Có xuất hiện không, vị trí đặt từ khóa, cách chèn tự nhiên |
| Từ khóa trong H1 | Có xuất hiện không, chèn tự nhiên không |
| Từ khóa trong 100 từ đầu | Xuất hiện ở phần mở đầu bài viết |
| Từ khóa trong H2/H3 | Xuất hiện ở ít nhất một tiêu đề phụ H2 hoặc H3 |
| Từ khóa trong Meta Description | Xuất hiện tự nhiên không bị nhồi nhét |
| Từ khóa trong URL | Có xuất hiện trong đường dẫn URL |
| Mật độ từ khóa (Density) | Tối ưu nhất từ 1-2%. Nhồi nhét trên 3% sẽ bị Google phạt. |

#### Từ khóa phụ (Secondary Keywords)
Xác định 5-10 từ khóa liên quan cần chèn tự nhiên vào nội dung:
- Các từ đồng nghĩa và biến thể của từ khóa chính.
- Từ khóa đuôi dài (long-tail keywords).
- Các câu hỏi liên quan khách hàng hay tìm kiếm (phần People Also Ask của Google).
- Từ khóa LSI (Latent Semantic Indexing).

#### Phân tích Khớp ý định tìm kiếm (Search Intent Alignment)
Xác định ý định thực tế đằng sau từ khóa chính và đánh giá mức độ đáp ứng của nội dung:

| Loại Search Intent | Mục tiêu của người dùng | Nội dung trang nên là |
|---|---|---|
| Informational (Thông tin) | Muốn học hỏi, giải đáp thắc mắc | Bài viết blog, cẩm nang hướng dẫn, FAQ |
| Commercial (Thương mại) | Muốn so sánh, lựa chọn gói | Trang so sánh, đánh giá, danh sách top giải pháp |
| Transactional (Giao dịch) | Muốn mua hàng | Trang chi tiết sản phẩm, trang bảng giá, trang thanh toán |
| Navigational (Điều hướng) | Muốn tìm một trang cụ thể | Trang chủ, trang đăng nhập, trang công cụ |

**Lệch Search Intent là lý do khiến bài viết không thể lên top.** Nếu người dùng tìm kiếm "cách làm X" (informational) nhưng link trỏ tới lại là trang bán dịch vụ (transactional), họ sẽ thoát trang ngay lập tức -- và thuật toán Google sẽ ghi nhận điều này để hạ hạng trang web.

### Bước 5: Kiểm tra nhanh Kỹ thuật SEO (Technical SEO)

#### File Robots.txt
```
Kiểm tra: Đường dẫn /robots.txt có tồn tại và cấu hình đúng chuẩn không?
```
- [ ] Robots.txt có thể truy cập được.
- [ ] Không chặn (disallow) các trang quan trọng hoặc các file tài nguyên hiển thị giao diện.
- [ ] Có trỏ link dẫn đến file sitemap.xml.
- [ ] Không chặn bot quét CSS/JS (vì Googlebot cần render trang hoàn chỉnh để đánh giá mobile-friendly).

#### XML Sitemap
```
Kiểm tra: Đường dẫn /sitemap.xml có tồn tại không?
```
- [ ] Sitemap hoạt động bình thường.
- [ ] Chứa đầy đủ danh sách các trang quan trọng của website.
- [ ] Không chứa link lỗi 404 trong sitemap.
- [ ] File sitemap đã được khai báo trên công cụ Google Search Console.
- [ ] Ngày cập nhật gần nhất (lastmod) hiển thị chính xác.

#### Thẻ Canonical
- [ ] Thẻ Canonical xuất hiện trên trang.
- [ ] Trỏ chính xác đến link URL gốc của trang (tự tham chiếu hoặc trỏ đến bản chính nếu là trang copy).
- [ ] Khớp cấu trúc link khai báo trong sitemap và file robots.txt.

#### Tốc độ tải trang
Tham chiếu chỉ số benchmark tốc độ chuẩn:

| Chỉ số | Tốt (Good) | Cần tối ưu | Kém (Poor) |
|---|---|---|---|
| Largest Contentful Paint (LCP) | Dưới 2.5 giây | 2.5-4.0 giây | Trên 4.0 giây |
| First Input Delay (FID) | Dưới 100ms | 100-300ms | Trên 300ms |
| Cumulative Layout Shift (CLS) | Dưới 0.1 | 0.1-0.25 | Trên 0.25 |
| Time to First Byte (TTFB) | Dưới 200ms | 200-500ms | Trên 500ms |
| First Contentful Paint (FCP) | Dưới 1.8 giây | 1.8-3.0 giây | Trên 3.0 giây |

**Các lỗi kỹ thuật gây chậm trang cần lưu ý:**
- Ảnh quá nặng (khuyên dùng định dạng WebP, bật nén ảnh).
- CSS/JS chặn hiển thị trang (render-blocking).
- Chưa cấu hình lưu bộ nhớ đệm (caching).
- Chưa sử dụng mạng CDN.
- Cài đặt quá nhiều script bên thứ ba (các mã theo dõi, font chữ bên ngoài, widget hỗ trợ).
- File code CSS/JS chưa được nén gọn.

#### Thân thiện thiết bị di động (Mobile-Friendly)
- [ ] Có cài đặt thẻ viewport meta tag (`<meta name="viewport" content="width=device-width, initial-scale=1">`).
- [ ] Cỡ chữ hiển thị dễ đọc không cần zoom (chữ body tối thiểu đạt 16px).
- [ ] Điểm chạm nút bấm đủ lớn và giãn cách hợp lý (tối thiểu đạt 48x48px).
- [ ] Bố cục giao diện co giãn tốt, không bị tràn cuộn ngang.
- [ ] Ảnh co giãn tự động theo khung màn hình (responsive images).
- [ ] Form đăng ký dễ điền trên giao diện mobile.

### Bước 6: Phân tích Khoảng trống Nội dung (Content Gap Analysis)

Phương pháp tìm kiếm các khoảng trống nội dung:
1. **Xác định cụm chủ đề (Topic Cluster):** Chủ đề lớn cốt lõi mà website đang muốn phủ sóng là gì?
2. **Lập sơ đồ nội dung hiện có:** Những subtopic (chủ đề phụ) nào đã được viết bài?
3. **Tìm lỗ hổng nội dung:** Những chủ đề phụ nào đối thủ viết rất tốt nhưng website của bạn chưa có bài viết?
4. **Khai thác phần People Also Ask của Google:** Những câu hỏi thắc mắc nào người dùng hay hỏi xoay quanh chủ đề này?
5. **Khai thác các từ khóa gợi ý liên quan:** Google gợi ý thêm những từ khóa nào ở chân trang SERP?

**Bảng khoảng trống nội dung mẫu:**
| Chủ đề còn thiếu | Lượng tìm kiếm tiềm năng | Mức độ cạnh tranh | Loại nội dung đề xuất | Độ ưu tiên |
|---|---|---|---|---|
| [Chủ đề] | Cao/Vừa/Thấp | Cao/Vừa/Thấp | Blog/Hướng dẫn/Công cụ/Page | 1-5 |

### Bước 7: Cơ hội giật top Feature Snippet

Xác định cơ hội để bài viết được hiển thị ở vị trí top 0 (Featured Snippet) của Google:

**Các định dạng Featured Snippet phổ biến:**
1. **Dạng đoạn văn (Paragraph):** Câu trả lời ngắn gọn trong 40-60 từ. Thiết lập tiêu đề dạng câu hỏi cụ thể (H2/H3) và trả lời trực diện súc tích ngay dòng tiếp theo.
2. **Dạng danh sách (List):** Sử dụng danh sách liệt kê có số thứ tự hoặc gạch đầu dòng, với thẻ H2 chứa câu hỏi tìm kiếm.
3. **Dạng bảng biểu (Table):** Sử dụng bảng dữ liệu HTML sạch có tiêu đề cột rõ ràng.
4. **Dạng video:** Đưa video lên bài viết có tiêu đề mô tả rõ và phân đoạn mốc thời gian (timestamps).

### Bước 8: Kiểm tra cài đặt Schema Markup

Đánh giá hiện trạng cài đặt dữ liệu cấu trúc:

| Loại Schema | Trang áp dụng phù hợp | Trạng thái |
|---|---|---|
| Organization (Tổ chức) | Trang chủ, trang giới thiệu | Đã cài/Chưa có |
| LocalBusiness (Doanh nghiệp địa phương) | Doanh nghiệp có địa chỉ vật lý | Đã cài/Chưa có/Không áp dụng |
| Product (Sản phẩm) | Các trang chi tiết sản phẩm | Đã cài/Chưa có/Không áp dụng |
| Article (Bài viết) | Bài viết blog, tin tức | Đã cài/Chưa có/Không áp dụng |
| FAQ (Câu hỏi thường gặp) | Phần giải đáp thắc mắc FAQ | Đã cài/Chưa có |
| HowTo (Hướng dẫn) | Các bài viết hướng dẫn từng bước | Đã cài/Chưa có/Không áp dụng |
| Review/AggregateRating | Đánh giá sao, testimonial | Đã cài/Chưa có/Không áp dụng |
| BreadcrumbList | Tất cả các trang con có thanh breadcrumb | Đã cài/Chưa có |
| WebSite/SearchAction | Trang chủ (tạo ô tìm kiếm sitelinks search box) | Đã cài/Chưa có |

**Hướng dẫn triển khai Schema:**
- Định dạng JSON-LD (được Google khuyên dùng).
- Kiểm tra tính hợp lệ bằng công cụ Rich Results Test của Google.
- Tuyệt đối không đánh dấu Schema cho những thông tin không hiển thị trực tiếp trên giao diện trang.
- Giữ thông tin trong Schema khớp chính xác với câu từ hiển thị trên trang.

---

## Định dạng Đầu ra: SEO-AUDIT.md

Lưu báo cáo vào file `SEO-AUDIT.md` trong thư mục hiện tại:

```markdown
# Báo cáo Audit SEO nội dung
## Trang phân tích: [URL]
### Ngày thực hiện: [Ngày tháng]

---

## Điểm sức khỏe SEO: [X/100]

---

## Checklist On-Page SEO

### Thẻ Title
- Trạng thái: [Đạt/Cần tối ưu/Chưa đạt]
- Hiện tại: "[nội dung thẻ title cũ]"
- Đề xuất thay thế: "[nội dung đề xuất tối ưu]"
- Các vấn đề phát hiện: [liệt kê lỗi nếu có]

### Thẻ Meta Description
- Trạng thái: [Đạt/Cần tối ưu/Chưa đạt]
- Hiện tại: "[meta description cũ]"
- Đề xuất thay thế: "[meta description đề xuất]"

### Phân cấp tiêu đề (Heading Hierarchy)
[Phân tích chi tiết cấu trúc thẻ H1-H6]

### Tối ưu hóa Hình ảnh
[Đánh giá Alt text, dung lượng ảnh, tên file, v.v.]

### Liên kết nội bộ (Internal Linking)
[Phân tích luồng link nội bộ trỏ tới trang và trỏ đi]

### Cấu trúc URL
[Đánh giá đường dẫn URL và đề xuất nếu cần]

---

## Chất lượng nội dung theo chuẩn E-E-A-T
| Khía cạnh | Chấm điểm | Bằng chứng thực tế thu thập được |
|---|---|---|
| Experience | [Mạnh/Đạt/Yếu/Chưa có] | [chi tiết cụ thể] |
| Expertise | [Mạnh/Đạt/Yếu/Chưa có] | [chi tiết] |
| Authoritativeness | [Mạnh/Đạt/Yếu/Chưa có] | [chi tiết] |
| Trustworthiness | [Mạnh/Đạt/Yếu/Chưa có] | [chi tiết] |

---

## Phân tích Từ khóa (Keyword Analysis)
- Từ khóa chính nhắm tới: [từ khóa]
- Ý định tìm kiếm (Search Intent): [loại intent]
- Tình trạng chèn từ khóa: [bảng đối chiếu các vị trí chèn]
- Danh sách từ khóa phụ đề xuất thêm: [danh sách từ khóa]

---

## Phân tích Kỹ thuật SEO (Technical SEO)
[Kết quả kiểm tra robots.txt, sitemap, canonical, tốc độ trang, mobile-friendly]

---

## Phân tích Khoảng trống Nội dung (Content Gap Analysis)
[Bảng các chủ đề đối thủ viết tốt nhưng website của bạn đang bị thiếu bài viết]

---

## Cơ hội giành vị trí Feature Snippet
[Các câu hỏi, bảng dữ liệu cụ thể trên trang có khả năng giật top Featured Snippet]

---

## Cấu trúc Schema Markup khuyên dùng
[So sánh schema hiện tại và các schema cần bổ sung]

---

## Khuyến nghị tối ưu liên kết nội bộ
[Đề xuất các trang hub, các liên kết context chất lượng nên trỏ tới trang này]

---

## Đánh giá Tốc độ trang Core Web Vitals
[Chỉ số hiệu suất tải trang và ước tính tác động doanh thu tăng thêm khi tải nhanh hơn]

---

## Đề xuất Chiến lược phát triển Nội dung lâu dài
[Tần suất xuất bản bài viết, các cụm chủ đề cần ưu tiên phủ sóng]

---

## Kế hoạch sửa đổi SEO theo thứ tự ưu tiên

### Nghiêm trọng (Sửa đổi ngay lập tức trong tuần này)
1. [Khuyến nghị cụ thể kèm theo tác động kỳ vọng]

### Ưu tiên cao (Thực hiện trong tháng này)
1. [Khuyến nghị cải tiến]

### Ưu tiên trung bình (Thực hiện trong quý này)
1. [Khuyến nghị]

### Ưu tiên thấp (Sắp xếp thực hiện khi có dư tài nguyên)
1. [Khuyến nghị]
```

## Các nguyên tắc cốt lõi

- Báo cáo audit SEO không chỉ đưa ra chẩn đoán lỗi mà cần mang tính giáo dục khách hàng. Hãy giải thích rõ TẠI SAO mỗi yếu tố lại quan trọng để chủ doanh nghiệp hiểu rõ giá trị công việc của bạn.
- Luôn cung cấp trực quan phần đối chứng "Before" (trạng thái lỗi cũ) và "After" (khuyến nghị đề xuất mới) để lập trình viên hoặc copywriter của khách hàng dễ dàng cập nhật.
- Kết nối các chỉ số SEO trực tiếp với kết quả kinh doanh thực tế. Việc giải thích "tối ưu thẻ Title giúp tăng tỷ lệ nhấp chuột CTR thêm 20-35%, đem lại thêm khoảng 500 lượng traffic chất lượng mỗi tháng" sẽ thuyết phục chủ doanh nghiệp hơn nhiều so với việc chỉ nói "thẻ Title đang bị thiếu từ khóa".
- Ưu tiên các khuyến nghị dựa trên tỷ lệ giữa công sức thực hiện và tác động mang lại. Ví dụ: sửa đổi thẻ Title và Meta Description chỉ tốn 5 phút nhưng có ảnh hưởng trực tiếp đến hàng nghìn lượt hiển thị tìm kiếm.
