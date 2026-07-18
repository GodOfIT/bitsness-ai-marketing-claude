# Tạo Đề xuất Dịch vụ Marketing gửi Khách hàng (Client Proposal Generator)

## Mục tiêu Kỹ năng

Tạo ra một đề xuất dịch vụ marketing (Client Proposal) chuyên nghiệp, sẵn sàng gửi trực tiếp cho khách hàng. Kỹ năng này xây dựng một tài liệu đề xuất hoàn chỉnh giúp định vị thương hiệu Bitsness (hoặc đối tác) là lựa chọn tối ưu nhất, cấu trúc các gói giá dịch vụ theo phương án mỏ neo giá thông minh và đưa ra các dự phóng ROI cụ thể nhằm chứng minh hiệu quả khoản đầu tư của khách hàng.

## Khi nào sử dụng

- Người dùng muốn tạo một bản đề xuất dịch vụ gửi cho khách hàng marketing tiềm năng.
- Người dùng đã hoàn thành cuộc gọi tìm hiểu (discovery call) và cần chính thức hóa nội dung hợp tác.
- Người dùng muốn xây dựng một biểu mẫu đề xuất chuẩn cho marketing agency của họ.
- Được kích hoạt bởi lệnh `/market proposal` hoặc `/market proposal <tên khách hàng>`.

## Hướng dẫn thực hiện

### Bước 1: Thu thập thông tin đầu vào

Thu thập các thông tin chi tiết sau từ người dùng (hỏi nếu chưa được cung cấp):

**Thông tin về Khách hàng:**
1. Tên khách hàng và tên công ty.
2. Ngành nghề kinh doanh và mô hình hoạt động.
3. Tình hình marketing hiện tại (những việc họ đang triển khai).
4. Các nỗi đau hoặc thách thức lớn nhất đang gặp phải.
5. Mục tiêu hướng tới (doanh thu, tăng trưởng, lead, độ nhận diện).
6. Khoảng ngân sách dự kiến (nếu có).
7. Khung thời gian ra quyết định hợp tác.
8. Những người có thẩm quyền ra quyết định chính.

**Thông tin về Dịch vụ Đề xuất:**
1. Bạn đề xuất những dịch vụ gì? (SEO, chạy ads, content, social media, email marketing, marketing tổng thể).
2. Mô hình hợp tác đề xuất (phí duy trì retainer, theo dự án project, hay theo hiệu quả performance-based).
3. Khung thời gian triển khai đề xuất.
4. Các case study hoặc kết quả tương tự bạn từng đạt được.

**Nếu đã có dữ liệu audit:** Kiểm tra xem trước đó đã chạy lệnh `/market audit` cho website khách hàng chưa. Nếu có, hãy tự động đưa các phát hiện trong bản audit đó vào phần Phân tích Tình huống (Situation Analysis) để tăng tính thuyết phục bằng dữ liệu thực tế.

### Bước 2: Bộ câu hỏi gợi ý cho Cuộc gọi Tìm hiểu (Discovery Call)

Nếu người dùng chưa thực hiện cuộc gọi tìm hiểu với khách hàng, hãy cung cấp cho họ 10 câu hỏi cốt lõi sau:

**Tìm hiểu Doanh nghiệp:**
1. "Xin vui lòng chia sẻ thêm về mô hình kinh doanh của bên mình. Doanh nghiệp tạo ra doanh thu chính từ nguồn nào?"
2. "Khách hàng lý tưởng của bên mình là ai? Bạn có thể mô tả chi tiết về họ không?"
3. "Quy trình bán hàng thực tế từ điểm chạm đầu tiên đến khi chốt hợp đồng của bên mình diễn ra như thế nào?"

**Tình hình Marketing hiện tại:**
4. "Hiện tại bên mình đang triển khai các hoạt động marketing nào? Kênh nào đang hiệu quả hoặc chưa hiệu quả?"
5. "Ngân sách chi tiêu marketing hàng tháng hiện tại là bao nhiêu và ROI đạt được như thế nào?"
6. "Bên mình đang sử dụng các công cụ và nền tảng công nghệ nào?"

**Mục tiêu và Kỳ vọng:**
7. "Nếu sự hợp tác của chúng ta đạt kết quả vượt bậc, bức tranh đó sẽ như thế nào sau 6 tháng? 12 tháng?"
8. "Các con số cụ thể bên mình muốn hướng tới là gì? (Doanh thu, số lượng lead, lượng traffic)"
9. "Giá trị trọn đời của một khách hàng (LTV) đối với doanh nghiệp của bạn là bao nhiêu?"

**Quy trình Ra quyết định:**
10. "Ngoài bạn ra thì còn ai tham gia vào việc phê duyệt đề xuất này không, và khung thời gian dự kiến để chọn đối tác là khi nào?"

**Câu hỏi bổ sung giá trị:**
- "Nỗi thất vọng lớn nhất của bạn đối với hoạt động marketing hiện tại là gì?"
- "Trước đây bên mình từng hợp tác với agency hay consultant nào chưa? Trải nghiệm tốt hay chưa tốt ở điểm nào?"
- "Có rào cản nào khiến bên mình có thể từ chối cơ hội hợp tác lần này không?"

### Bước 3: Xây dựng cấu trúc tài liệu Đề xuất

#### Phần 1: Trang bìa (Cover Page)
```
[Logo của bạn / Bitsness]

ĐỀ XUẤT CHIẾN LƯỢC MARKETING
Dành cho: [Tên khách hàng]
Được thực hiện bởi: [Tên của bạn / Agency / Bitsness]
Ngày thực hiện: [Ngày tháng]
Thời hạn hiệu lực: [Ngày tháng + 30 ngày]

TÀI LIỆU BẢO MẬT
```

#### Phần 2: Tóm tắt Điều hành (Executive Summary) (Tối đa 1 trang)
Viết một đoạn tóm tắt ngắn gọn nhằm:
- Xác nhận hoàn cảnh hiện tại và mục tiêu của khách hàng.
- Nêu rõ vấn đề cốt lõi mà bạn sẽ giải quyết.
- Khái quát cách tiếp cận đề xuất của bạn.
- Hé lộ kết quả kỳ vọng đạt được.
- Tạo động lực khẩn cấp để khách hành động ngay.

**Mẫu viết:**
```
[Tên doanh nghiệp đối tác] đang ở một thời điểm chuyển dịch quan trọng. Với [hoàn cảnh hiện tại -- ví dụ: sản phẩm có độ khớp thị trường tốt nhưng kênh thu hút lead chưa ổn định], đây là cơ hội lớn để bên mình có thể [kết quả mong muốn -- ví dụ: tăng quy mô thu hút khách hàng mới nhằm đạt chỉ tiêu tăng trưởng năm].

Dựa trên phân tích của chúng tôi đối với [các thành phần đã quét -- website, ads, đối thủ, v.v.], chúng tôi xác định được [X] cơ hội lớn để tối ưu chiến lược giúp mang lại [kết quả cụ thể -- ví dụ: tăng từ 40-60% lượng lead chất lượng trong vòng 6 tháng].

Bản đề xuất này phác thảo hành trình hợp tác trong vòng [thời gian] tập trung vào [các mảng dịch vụ chính], được thiết kế để mang lại [kết quả chính]. Cách tiếp cận của chúng tôi dựa trên [điểm khác biệt của bạn -- ví dụ: phương pháp luận dựa trên dữ liệu thực tế, sự am hiểu sâu sắc về ngành, các khung lý thuyết đã chứng minh hiệu quả].

Chúng tôi đề xuất bắt đầu với [giai đoạn 1] để thiết lập các chỉ số nền tảng và gặt hái các chiến thắng nhanh (quick wins), sau đó sẽ tăng quy mô dựa trên số liệu hiệu quả thực tế.
```

#### Phần 3: Phân tích Tình huống (Situation Analysis) (2-3 trang)
Trình bày phân tích về hiện trạng marketing của khách hàng. Đây là nơi đưa dữ liệu từ lệnh `/market audit` vào để tăng tính thuyết phục.

**Cấu trúc:**
1. **Tổng quan Hiện trạng** -- Những gì họ đang làm và hiệu quả thực tế.
2. **Các cơ hội cải tiến phát hiện** -- Những khu vực cụ thể có khả năng tối ưu hóa.
3. **Bức tranh cạnh tranh** -- So sánh vị thế với đối thủ (lấy từ lệnh `/market competitors` nếu có).
4. **Các thách thức chính** -- Các rào cản cần được tháo gỡ.
5. **Ngữ cảnh thị trường** -- Các xu hướng và chỉ số benchmark của ngành.

**Lưu ý quan trọng:** Luôn trình bày mọi thứ dưới dạng các "cơ hội cải tiến" thay vì đánh giá đó là một "thất bại". Khách hàng cần cảm thấy được thấu hiểu chứ không phải bị chỉ trích.

- Nên viết: "Website của bên mình hiện tại có tỷ lệ chuyển đổi khoảng 1.8%, thấp hơn mức trung bình của ngành là 3.2%. Chúng tôi nhìn thấy cơ hội rõ ràng để lấp đầy khoảng trống này bằng các chiến dịch tối ưu hóa CRO."
- Tránh viết: "Website của bên mình có tỷ lệ chuyển đổi quá kém và cần phải thiết kế lại toàn bộ."

#### Phần 4: Chiến lược và Cách tiếp cận (2-3 trang)
Trình bày chiến lược đề xuất của bạn. Hãy viết đủ chi tiết để chứng minh năng lực chuyên môn nhưng không quá chi tiết đến mức họ có thể tự làm mà không cần bạn.

**Cấu trúc:**
1. **Khung Chiến lược** -- Phương pháp luận và cách tiếp cận tổng thể của bạn.
2. **Giai đoạn 1: Nền tảng (Foundation)** (Tháng 1-2) -- Cài đặt, audit, lấy số liệu base, gặt hái quick wins.
3. **Giai đoạn 2: Tăng trưởng (Growth)** (Tháng 3-4) -- Triển khai các chiến dịch cốt lõi, tối ưu hóa liên tục.
4. **Giai đoạn 3: Tăng quy mô (Scale)** (Tháng 5-6) -- Đẩy mạnh mảng hiệu quả, cắt giảm mảng kém, đầu tư ngân sách vào kênh thắng cuộc.
5. **Vận hành định kỳ: Tối ưu** -- Cải tiến liên tục, làm báo cáo định kỳ, tinh chỉnh chiến lược.

Với mỗi giai đoạn, hãy nêu rõ:
- Các hoạt động và kết quả bàn giao cụ thể.
- Kết quả kỳ vọng đạt được.
- Cách đo lường sự thành công.

#### Phần 5: Phạm vi Công việc (Scope of Work) (1-2 trang)
Chi tiết hóa chính xác những gì được bao gồm trong gói dịch vụ (và những gì không bao gồm).

**Những gì bao gồm:**
- Các kết quả bàn giao cụ thể kèm số lượng (ví dụ: "Sản xuất 8 bài viết blog mỗi tháng, độ dài từ 1,500-2,000 từ mỗi bài").
- Tần suất họp hành trao đổi (ví dụ: "Họp chiến lược định kỳ 2 tuần một lần, gửi báo cáo hàng tháng").
- Cam kết thời gian phản hồi (ví dụ: "Phản hồi trong vòng 24 giờ vào các ngày làm việc").
- Các công cụ và phần mềm được bao gồm trong gói dịch vụ.
- Định dạng và tần suất gửi báo cáo.

**Những gì loại trừ (Explicitly Exclude):**
- Các đầu việc nằm ngoài phạm vi để tránh tình trạng phát sinh việc không tính phí (scope creep).
- Các chi phí bổ sung (ngân sách chạy ads, chi phí bản quyền phần mềm của khách, mua ảnh stock).
- Các giả định về trách nhiệm tự thân của khách hàng.

**Phần Trách nhiệm của Khách hàng:**
Liệt kê những gì bạn cần từ phía khách hàng để chiến dịch thành công:
- Phản hồi và duyệt nội dung đúng hạn (quy định rõ SLA số ngày).
- Cung cấp quyền truy cập tài khoản, công cụ và dữ liệu cần thiết.
- Chỉ định người đầu mối liên hệ chính.
- Duyệt nội dung trong vòng X ngày làm việc.
- Ngân sách chạy quảng cáo (thanh toán riêng biệt, độc lập với phí quản lý dịch vụ).

#### Phần 6: Lộ trình Triển khai (Timeline) (1 trang)
Lập lộ trình trực quan thể hiện các giai đoạn, cột mốc và kết quả bàn giao.

```
Tháng 1     | Tháng 2     | Tháng 3     | Tháng 4     | Tháng 5     | Tháng 6
------------|-------------|-------------|-------------|-------------|-----------
NỀN TẢNG    | NỀN TẢNG    | TĂNG TRƯỞNG | TĂNG TRƯỞNG | TĂNG QUY MÔ | TĂNG QUY MÔ
Audit &     | Quick wins  | Khởi chạy   | Tối ưu hóa  | Mở rộng     | Đẩy mạnh
Cài đặt     | & chỉ số base| Chiến dịch  | & lặp lại   | kênh thắng  | tối đa

Các Cột mốc quan trọng:
- Tuần 2: Hoàn thành tài liệu Audit và Chiến lược tổng thể.
- Tuần 4: Khởi chạy chiến dịch đầu tiên.
- Tháng 2: Gửi báo cáo hiệu suất đầu tiên.
- Tháng 3: Đưa ra các khuyến nghị tối ưu hóa phễu.
- Tháng 6: Đánh giá toàn diện và tinh chỉnh chiến lược cho giai đoạn tiếp theo.
```

#### Phần 7: Gói đầu tư (Investment) (1-2 trang)
Trình bày thông tin giá cả dịch vụ theo cấu trúc 3 gói (Good-Better-Best).

**Bảng so sánh 3 gói dịch vụ:**

| Hạng mục dịch vụ | Gói Growth (Tăng trưởng) | Gói Accelerate (Tăng tốc) | Gói Dominate (Thống lĩnh) |
|---|---|---|---|
| Chiến lược & Quy hoạch | Đánh giá hàng quý | Chiến lược hàng tháng | Chiến lược hàng tuần |
| Sáng tạo nội dung | 4 bài viết/tháng | 8 bài viết/tháng | 16 bài viết/tháng |
| Mạng xã hội (Social) | Quản lý 3 nền tảng | Quản lý 5 nền tảng | Toàn bộ các nền tảng |
| Quản lý Quảng cáo Ads | Ngân sách dưới $5K | Ngân sách dưới $15K | Ngân sách dưới $50K |
| Dịch vụ SEO | Tối ưu On-page cơ bản | Chương trình SEO toàn diện | SEO toàn diện + link building |
| Email Marketing | -- | Gửi newsletter hàng tháng | Tự động hóa phễu email |
| Báo cáo số liệu | Báo cáo hàng tháng | Báo cáo 2 tuần một lần | Dashboard thời gian thực |
| Họp định kỳ | Họp 1 lần/tháng | Họp 2 tuần một lần | Họp hàng tuần |
| **Phí Dịch vụ Hàng tháng** | **$X,XXX** | **$X,XXX** | **$X,XXX** |

**Tâm lý học Định giá:**
- Cung cấp 3 gói lựa chọn; hầu hết khách hàng sẽ xu hướng chọn gói ở giữa.
- Đặt tên các gói dịch vụ mang tính thúc đẩy, tham vọng (tránh đặt gói Đồng/Bạc/Vàng).
- Đặt gói có mức giá cao nhất lên đầu tiên để làm neo giá, giúp gói ở giữa có cảm giác hợp lý hơn.
- Gắn nhãn "Khuyên dùng" hoặc "Phổ biến nhất" vào gói ở giữa.
- Làm phép tính ROI trực quan: "Với chỉ số [LTV của khách], bên mình chỉ cần có thêm [X] khách hàng mới mỗi tháng để đạt mức ROI dương."

**Tham khảo các Mô hình tính phí:**

| Mô hình | Khi nào áp dụng | Khoảng giá phổ biến |
|---|---|---|
| Phí Retainer hàng tháng | Dịch vụ định kỳ, xây dựng quan hệ dài hạn | $2,000-$25,000/tháng |
| Theo Dự án (Project-based) | Định rõ phạm vi công việc, bàn giao một lần | $5,000-$100,000/dự án |
| Theo Hiệu quả (Performance) | Chia sẻ rủi ro, bạn rất tự tin vào kết quả | Phí cứng thấp + % doanh thu/lead |
| Mô hình Hybrid | Các dự án lớn phức tạp | Retainer cơ bản + bonus theo hiệu quả |
| Tính phí theo giờ | Tư vấn, cố vấn, công việc phát sinh | $150-$500/giờ |

#### Phần 8: Dự phóng hiệu quả ROI (ROI Projection)
Chứng minh cho khách hàng thấy mức lợi nhuận kỳ vọng từ khoản đầu tư của họ.

```
Hiện trạng hiện tại:
- Lượng truy cập web hàng tháng: [X]
- Tỷ lệ chuyển đổi hiện tại: [X%]
- Số lượng lead phát sinh/tháng: [X]
- Tỷ lệ chốt đơn (Close rate): [X%]
- Giá trị đơn hàng trung bình: $[X]
- Doanh thu hàng tháng hiện tại từ marketing: $[X]

Dự phóng mục tiêu (Sau 6 tháng):
- Dự kiến traffic tăng trưởng: [X%] -> [lượng traffic mới]
- Dự kiến tỷ lệ chuyển đổi: [X%] -> [lượng lead mới/tháng]
- Dự kiến lượng lead tăng trưởng: [X%]
- Doanh thu tăng thêm dự kiến: $[X]/tháng
- ROI dự kiến sau 6 tháng: đạt mức [X] lần

Mức đầu tư dịch vụ: $[tổng chi phí 6 tháng]
Doanh thu dự kiến đem lại: $[tổng doanh thu tăng thêm dự kiến]
Mức ROI đạt được: đạt mức [X] lần lợi nhuận
```

**Lưu ý quan trọng:** Hãy đưa ra các con số dự phóng một cách thận trọng. Nguyên tắc là hứa ít làm nhiều (under-promise and over-deliver). Hãy dùng khoảng dao động (ranges) thay vì đưa ra một con số cứng duy nhất. Đưa thêm các dòng miễn trừ trách nhiệm rằng kết quả thực tế còn phụ thuộc vào nhiều yếu tố vận hành của doanh nghiệp.

#### Phần 9: Đội ngũ nhân sự (Team) (0.5-1 trang)
Giới thiệu các thành viên chính sẽ trực tiếp vận hành dự án này.

Với mỗi nhân sự, cung cấp:
- Họ tên và chức danh.
- Kinh nghiệm và chuyên môn thế mạnh liên quan.
- Vai trò đảm nhiệm trong dự án này.
- Mô tả ngắn gọn về bản thân (tối đa 2-3 câu).

#### Phần 10: Case Studies tiêu biểu (1-2 trang)
Đưa vào 2-3 case study thực tế đã triển khai thành công đạt kết quả tương tự lời hứa của bạn.

**Định dạng Case Study:**
```
Khách hàng: [Lĩnh vực hoạt động và loại hình doanh nghiệp -- ẩn tên nếu cần bảo mật]
Thách thức gặp phải: [1-2 câu mô tả tình trạng khó khăn ban đầu của họ]
Giải pháp triển khai: [1-2 câu mô tả những việc bạn đã thực hiện]
Kết quả đạt được:
- [Chỉ số 1: ví dụ: "Tăng 287% lượng traffic tự nhiên trong 6 tháng"]
- [Chỉ số 2: ví dụ: "Giảm chi phí thu một lead (CPL) từ $45 xuống còn $12"]
- [Chỉ số 3: ví dụ: "Mang lại 180,000 USD doanh thu mới phát sinh"]
```

#### Phần 11: Các bước tiếp theo cần làm (0.5 trang)
Hướng dẫn chi tiết bước tiếp theo để bắt đầu hợp tác nhằm giảm thiểu tối đa ma sát ra quyết định.

```
Bạn đã sẵn sàng để bắt đầu đồng hành cùng chúng tôi? Dưới đây là bước tiếp theo:

1. Ký phê duyệt bản đề xuất này (đường link ký điện tử đính kèm phía dưới).
2. Chúng tôi sẽ lên lịch cuộc họp Kickoff khởi động dự án trong vòng 48 giờ.
3. Bạn sẽ nhận được bộ câu hỏi Onboarding và form yêu cầu cung cấp quyền truy cập.
4. Chúng tôi sẽ bắt tay triển khai Giai đoạn 1: Nền tảng ngay lập tức.

Nếu bạn có thắc mắc? Vui lòng liên hệ với [Họ tên] qua email [email] hoặc số điện thoại [sđt].

Bản đề xuất này có hiệu lực đến ngày [ngày tháng -- 30 ngày kể từ hôm nay].
```

### Bước 4: Thiết kế và Định dạng tài liệu Đề xuất

**Nguyên tắc chuyên nghiệp:**
- Giới hạn toàn bộ đề xuất dưới 15 trang (không tính phần phụ lục).
- Sử dụng nhất quán font chữ, tiêu đề và tông màu thương hiệu Bitsness xuyên suốt tài liệu.
- Đặt logo của khách hàng trang trọng bên cạnh logo của bạn/Bitsness trên trang bìa.
- Lồng ghép các sơ đồ, bảng biểu trực quan thay vì viết các đoạn văn bản dài khô khan.
- Bôi đậm các con số kết quả và chỉ số quan trọng.
- Sử dụng khoảng trắng hợp lý để tài liệu có độ thở dễ đọc, không nhồi nhét chữ.
- Đánh số trang đầy đủ và có mục lục rõ ràng đối với đề xuất dài.
- Xuất file định dạng PDF chuyên nghiệp để gửi khách hàng.

---

## Định dạng Đầu ra: CLIENT-PROPOSAL.md

Ghi toàn bộ kết quả vào file `CLIENT-PROPOSAL.md`:

```markdown
# Đề xuất Dịch vụ Marketing chuyên nghiệp

## Dành cho: [Tên khách hàng]
## Thực hiện bởi: [Tên Agency / Bitsness]
## Ngày thực hiện: [Ngày tháng]

---

## Mục lục
1. Tóm tắt Điều hành (Executive Summary)
2. Phân tích Hiện trạng (Situation Analysis)
3. Chiến lược & Cách tiếp cận
4. Phạm vi Công việc (Scope of Work)
5. Lộ trình Triển khai (Timeline)
6. Gói Đầu tư (Investment)
7. Dự phóng hiệu quả ROI
8. Đội ngũ Nhân sự
9. Các Case Study tiêu biểu
10. Các bước tiếp theo để bắt đầu

---

[Nội dung chi tiết của bản đề xuất được điền đầy đủ dựa trên thông tin thực tế của khách hàng]

---

## Phụ lục
- Các Điều khoản & Điều kiện pháp lý
- Mô tả chi tiết các kết quả bàn giao
- Hệ thống công nghệ sử dụng (Tool Stack)
```

## Các nguyên tắc cốt lõi

- Bản đề xuất là một tài liệu bán hàng (sales document), không đơn thuần là một bản mô tả công việc (statement of work). Nó phải thuyết phục và BÁN HÀNG, chứ không chỉ liệt kê đầu việc.
- Luôn bắt đầu từ vấn đề và mục tiêu của khách hàng, đừng bắt đầu từ việc giới thiệu dịch vụ của bạn. Hãy làm cho họ thấy họ được thấu hiểu sâu sắc trước khi đưa ra giải pháp.
- Mọi mức giá đưa ra đều phải được neo giữ (anchor) với giá trị ROI mà nó sẽ tạo ra. Tuyệt đối không đưa ra chi phí khơi khơi mà không gắn với ngữ cảnh giá trị mang lại.
- Sử dụng đúng ngôn từ và thuật ngữ khách hàng đã nói trong cuộc gọi tìm hiểu để tạo sự đồng điệu.
- Nếu có sẵn dữ liệu audit từ các bước trước, hãy khai thác tối đa — các bản đề xuất dựa trên số liệu thực tế có tỷ lệ chốt thành công cao gấp 2-3 lần thông thường.
- Luôn chỉ ra một bước tiếp theo cực kỳ rõ ràng, có giới hạn thời gian hiệu lực để thúc đẩy chốt hợp đồng. Sự mơ hồ là kẻ thù giết chết mọi thương vụ.
