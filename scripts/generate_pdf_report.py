#!/usr/bin/env python3
"""
Marketing Report PDF Generator — Bitsness AI Marketing Suite
Generates professional, client-ready PDF marketing reports with charts,
score visualizations, and prioritized action plans.

Requires: reportlab (pip install reportlab)
"""

import sys
import json
import os
from datetime import datetime

try:
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.units import inch
    from reportlab.lib.colors import HexColor, white, black
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                     TableStyle, PageBreak, Image)
    from reportlab.graphics.shapes import Drawing, Rect, Circle, String, Line, Wedge
    from reportlab.graphics.charts.barcharts import VerticalBarChart
    from reportlab.graphics import renderPDF
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
except ImportError:
    print("Error: reportlab is required. Install with: pip install reportlab")
    sys.exit(1)


# Color palette
COLORS = {
    "primary": HexColor("#1B2A4A"),
    "accent": HexColor("#2D5BFF"),
    "highlight": HexColor("#FF6B35"),
    "success": HexColor("#00C853"),
    "warning": HexColor("#FFB300"),
    "danger": HexColor("#FF1744"),
    "light_bg": HexColor("#F5F7FA"),
    "text": HexColor("#2C3E50"),
    "text_light": HexColor("#7F8C9B"),
    "border": HexColor("#E0E6ED"),
    "white": white,
    "black": black,
}


def register_unicode_fonts():
    """Register system fonts supporting Vietnamese accents."""
    font_paths_regular = [
        r"C:\Windows\Fonts\arial.ttf",
        "/Library/Fonts/Arial.ttf",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    ]
    font_paths_bold = [
        r"C:\Windows\Fonts\arialbd.ttf",
        "/Library/Fonts/Arial Bold.ttf",
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    ]
    
    # Try registering regular font
    reg_registered = False
    for path in font_paths_regular:
        if os.path.exists(path):
            try:
                pdfmetrics.registerFont(TTFont("ArialUnicode", path))
                reg_registered = True
                break
            except Exception:
                pass
    if not reg_registered:
        # Fallback to Helvetica
        pdfmetrics.registerFont(TTFont("ArialUnicode", "Helvetica"))
        
    # Try registering bold font
    bold_registered = False
    for path in font_paths_bold:
        if os.path.exists(path):
            try:
                pdfmetrics.registerFont(TTFont("ArialUnicode-Bold", path))
                bold_registered = True
                break
            except Exception:
                pass
    if not bold_registered:
        # Fallback to Helvetica-Bold
        pdfmetrics.registerFont(TTFont("ArialUnicode-Bold", "Helvetica-Bold"))


# Register fonts immediately
register_unicode_fonts()


# Category Map to translate keys into Vietnamese
CATEGORY_MAP = {
    "Content & Messaging": "Content & Messaging (Nội dung)",
    "Conversion Optimization": "Tối ưu hóa Chuyển đổi (CRO)",
    "SEO & Discoverability": "SEO & Khả năng Hiển thị",
    "Competitive Positioning": "Định vị Cạnh tranh",
    "Brand & Trust": "Thương hiệu & Sự tin cậy",
    "Growth & Strategy": "Chiến lược & Tăng trưởng"
}


def score_color(score):
    """Return color based on score value."""
    if score >= 80:
        return COLORS["success"]
    elif score >= 60:
        return COLORS["accent"]
    elif score >= 40:
        return COLORS["warning"]
    else:
        return COLORS["danger"]


def draw_score_gauge(score, x, y, size=80):
    """Create a circular score gauge drawing."""
    d = Drawing(size + 20, size + 30)

    # Background circle
    d.add(Circle(size / 2 + 10, size / 2 + 15, size / 2,
                 fillColor=COLORS["light_bg"], strokeColor=COLORS["border"], strokeWidth=2))

    # Score arc (simplified as colored inner circle)
    color = score_color(score)
    inner_r = size / 2 - 8
    d.add(Circle(size / 2 + 10, size / 2 + 15, inner_r,
                 fillColor=color, strokeColor=None))

    # White center
    d.add(Circle(size / 2 + 10, size / 2 + 15, inner_r - 10,
                 fillColor=COLORS["white"], strokeColor=None))

    # Score text
    d.add(String(size / 2 + 10, size / 2 + 10, str(int(score)),
                 fontSize=20, fillColor=COLORS["primary"],
                 textAnchor="middle", fontName="ArialUnicode-Bold"))

    return d


def create_bar_chart(categories, scores, width=450, height=180):
    """Create a horizontal bar chart for category scores."""
    d = Drawing(width, height)

    bar_height = 20
    gap = 8
    max_bar_width = width - 180
    start_y = height - 30
    label_x = 5
    bar_x = 160

    for i, (cat, score) in enumerate(zip(categories, scores)):
        y = start_y - i * (bar_height + gap)

        # Translate category if mapping exists
        cat_display = CATEGORY_MAP.get(cat, cat)

        # Category label
        d.add(String(label_x, y + 5, cat_display[:26],
                     fontSize=9, fillColor=COLORS["text"],
                     textAnchor="start", fontName="ArialUnicode"))

        # Background bar
        d.add(Rect(bar_x, y, max_bar_width, bar_height,
                   fillColor=COLORS["light_bg"], strokeColor=None))

        # Score bar
        bar_width = (score / 100) * max_bar_width
        color = score_color(score)
        d.add(Rect(bar_x, y, bar_width, bar_height,
                   fillColor=color, strokeColor=None))

        # Score label
        d.add(String(bar_x + max_bar_width + 10, y + 5, f"{int(score)}",
                     fontSize=10, fillColor=COLORS["text"],
                     textAnchor="start", fontName="ArialUnicode-Bold"))

    return d


def generate_report(data, output_path):
    """Generate a professional marketing PDF report."""
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        rightMargin=50,
        leftMargin=50,
        topMargin=50,
        bottomMargin=50
    )

    styles = getSampleStyleSheet()

    # Custom styles using ArialUnicode
    title_style = ParagraphStyle(
        "CustomTitle",
        parent=styles["Title"],
        fontSize=26,
        textColor=COLORS["primary"],
        spaceAfter=6,
        fontName="ArialUnicode-Bold"
    )

    subtitle_style = ParagraphStyle(
        "CustomSubtitle",
        parent=styles["Normal"],
        fontSize=12,
        textColor=COLORS["text_light"],
        spaceAfter=20,
        fontName="ArialUnicode"
    )

    heading_style = ParagraphStyle(
        "CustomHeading",
        parent=styles["Heading1"],
        fontSize=18,
        textColor=COLORS["primary"],
        spaceBefore=20,
        spaceAfter=10,
        fontName="ArialUnicode-Bold"
    )

    subheading_style = ParagraphStyle(
        "CustomSubheading",
        parent=styles["Heading2"],
        fontSize=14,
        textColor=COLORS["accent"],
        spaceBefore=14,
        spaceAfter=8,
        fontName="ArialUnicode-Bold"
    )

    body_style = ParagraphStyle(
        "CustomBody",
        parent=styles["Normal"],
        fontSize=10,
        textColor=COLORS["text"],
        spaceAfter=6,
        fontName="ArialUnicode",
        leading=14
    )

    # Build document elements
    elements = []

    # === LOGO HANDLING ===
    # Check for logo.jpg in root or current folder
    logo_path = None
    possible_logo_paths = [
        "resources/logo.jpg",
        "../resources/logo.jpg",
        os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "resources", "logo.jpg"),
        os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "logo.jpg"),
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "logo.jpg"),
        r"c:\Users\phamd\Desktop\ai-marketing-claude\resources\logo.jpg"
    ]
    for p in possible_logo_paths:
        if os.path.exists(p):
            logo_path = p
            break

    if logo_path:
        try:
            elements.append(Image(logo_path, width=150, height=60))
            elements.append(Spacer(1, 0.2 * inch))
        except Exception as e:
            print(f"Warning: Could not add logo image to PDF: {e}")

    # === COVER PAGE ===
    elements.append(Paragraph("Báo cáo Đánh giá Marketing Bitsness", title_style))

    url = data.get("url", "example.com")
    date_str = data.get("date", datetime.now().strftime("%d/%m/%Y"))
    elements.append(Paragraph(f"Trang web phân tích: {url}", subtitle_style))
    elements.append(Paragraph(f"Ngày lập báo cáo: {date_str}", subtitle_style))
    elements.append(Spacer(1, 0.3 * inch))

    # Overall score gauge
    overall_score = data.get("overall_score", 0)
    gauge = draw_score_gauge(overall_score, 0, 0, size=100)
    elements.append(gauge)
    elements.append(Spacer(1, 0.2 * inch))

    grade = "A+" if overall_score >= 90 else "A" if overall_score >= 80 else "B" if overall_score >= 70 else "C" if overall_score >= 60 else "D" if overall_score >= 50 else "F"
    elements.append(Paragraph(f"Điểm Marketing Tổng thể: {int(overall_score)}/100 (Hạng: {grade})", heading_style))

    exec_summary = data.get("executive_summary", "Báo cáo này cung cấp cái nhìn toàn diện về hiệu quả marketing của website trên các danh mục cốt lõi bao gồm nội dung, tối ưu chuyển đổi, cấu trúc SEO, vị thế cạnh tranh, niềm tin thương hiệu và chiến lược tăng trưởng.")
    elements.append(Paragraph(exec_summary, body_style))

    elements.append(PageBreak())

    # === SCORE BREAKDOWN ===
    elements.append(Paragraph("Chi tiết Điểm số", heading_style))

    categories = data.get("categories", {})
    cat_names = list(categories.keys()) if categories else [
        "Content & Messaging", "Conversion Optimization", "SEO & Discoverability",
        "Competitive Positioning", "Brand & Trust", "Growth & Strategy"
    ]
    cat_scores = [categories.get(c, {}).get("score", 50) for c in cat_names] if categories else [65, 58, 72, 55, 68, 60]

    # Bar chart
    chart = create_bar_chart(cat_names, cat_scores)
    elements.append(chart)
    elements.append(Spacer(1, 0.3 * inch))

    # Score table
    score_data = [["Danh mục", "Điểm số", "Trọng số", "Trạng thái"]]
    weights = ["25%", "20%", "20%", "15%", "10%", "10%"]
    
    status_map = {
        "Strong": "Tốt",
        "Needs Work": "Cần tối ưu",
        "Critical": "Yếu kém"
    }

    for i, (name, score) in enumerate(zip(cat_names, cat_scores)):
        status = "Strong" if score >= 75 else "Needs Work" if score >= 50 else "Critical"
        status_vietnamese = status_map.get(status, status)
        weight = weights[i] if i < len(weights) else "—"
        name_vietnamese = CATEGORY_MAP.get(name, name)
        score_data.append([name_vietnamese, f"{int(score)}/100", weight, status_vietnamese])

    score_table = Table(score_data, colWidths=[200, 60, 60, 80])
    score_table.setStyle(TableStyle([
        ("FONTNAME", (0, 0), (-1, -1), "ArialUnicode"),
        ("BACKGROUND", (0, 0), (-1, 0), COLORS["primary"]),
        ("TEXTCOLOR", (0, 0), (-1, 0), COLORS["white"]),
        ("FONTNAME", (0, 0), (-1, 0), "ArialUnicode-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("ALIGN", (1, 0), (-1, -1), "CENTER"),
        ("GRID", (0, 0), (-1, -1), 0.5, COLORS["border"]),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [COLORS["white"], COLORS["light_bg"]]),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    elements.append(score_table)

    elements.append(PageBreak())

    # === KEY FINDINGS ===
    elements.append(Paragraph("Các phát hiện chính", heading_style))

    findings = data.get("findings", [])
    if not findings:
        findings = [
            {"severity": "Critical", "finding": "Tiêu đề trang chủ chưa rõ ràng — khách truy cập không hiểu giá trị sản phẩm trong vòng 5 giây"},
            {"severity": "High", "finding": "Thiếu các bằng chứng xã hội (Social Proof) như testimonial, đánh giá hoặc logo đối tác"},
            {"severity": "High", "finding": "Nút CTA chính sử dụng chữ chung chung ('Gửi đi') thay vì hướng lợi ích giá trị"},
            {"severity": "Medium", "finding": "Thiếu thẻ Meta Description trên một số trang dịch vụ chính"},
            {"severity": "Medium", "finding": "Chưa có cơ chế thu thập email hoặc mồi dẫn dụ (Lead Magnet) hữu ích"},
            {"severity": "Low", "finding": "Các bài viết blog thiếu liên kết nội bộ hướng tới trang sản phẩm dịch vụ"},
        ]

    findings_data = [["Mức độ", "Phát hiện lỗi"]]
    
    severity_map = {
        "Critical": "Nghiêm trọng",
        "High": "Cao",
        "Medium": "Trung bình",
        "Low": "Thấp"
    }

    for f in findings:
        severity = f.get("severity", "Medium")
        severity_vietnamese = severity_map.get(severity, severity)
        finding = f.get("finding", "")
        findings_data.append([severity_vietnamese, Paragraph(finding, body_style)])

    findings_table = Table(findings_data, colWidths=[80, 390])
    severity_colors = {
        "Critical": COLORS["danger"],
        "High": COLORS["highlight"],
        "Medium": COLORS["warning"],
        "Low": COLORS["accent"]
    }
    
    table_style_cmds = [
        ("FONTNAME", (0, 0), (-1, -1), "ArialUnicode"),
        ("BACKGROUND", (0, 0), (-1, 0), COLORS["primary"]),
        ("TEXTCOLOR", (0, 0), (-1, 0), COLORS["white"]),
        ("FONTNAME", (0, 0), (-1, 0), "ArialUnicode-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("GRID", (0, 0), (-1, -1), 0.5, COLORS["border"]),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("ALIGN", (0, 0), (0, -1), "CENTER"),
    ]
    for i, f in enumerate(findings, 1):
        color = severity_colors.get(f.get("severity", "Medium"), COLORS["warning"])
        table_style_cmds.append(("TEXTCOLOR", (0, i), (0, i), color))
        table_style_cmds.append(("FONTNAME", (0, i), (0, i), "ArialUnicode-Bold"))

    findings_table.setStyle(TableStyle(table_style_cmds))
    elements.append(findings_table)

    elements.append(PageBreak())

    # === ACTION PLAN ===
    elements.append(Paragraph("Kế hoạch Hành động Ưu tiên", heading_style))

    # Quick Wins
    elements.append(Paragraph("Chiến thắng nhanh (Tuần này)", subheading_style))
    quick_wins = data.get("quick_wins", [
        "Viết lại tiêu đề trang chủ tập trung vào lợi ích cụ thể khách hàng nhận được",
        "Bổ sung 3-5 logo đối tác uy tín hoặc trust badges lên màn hình đầu tiên",
        "Thay đổi chữ nút CTA chính hướng giá trị (Ví dụ: 'Bắt đầu dùng thử miễn phí')",
        "Bổ sung đầy đủ thẻ meta description cho 5 trang landing quan trọng nhất",
    ])
    for i, win in enumerate(quick_wins, 1):
        elements.append(Paragraph(f"{i}. {win}", body_style))

    elements.append(Spacer(1, 0.2 * inch))

    # Medium-Term
    elements.append(Paragraph("Trung hạn (1-3 Tháng)", subheading_style))
    medium_term = data.get("medium_term", [
        "Thiết lập phễu thu thập email đi kèm mồi dẫn dụ (Lead Magnet) hữu ích",
        "Xây dựng trang so sánh tính năng đối đầu với top 3 đối thủ cạnh tranh",
        "Biên soạn 3 case study khách hàng thành công có số liệu thực tế",
        "Triển khai chiến lược nội dung blog nhắm tới các từ khóa có ý định mua hàng cao",
    ])
    for i, action in enumerate(medium_term, 1):
        elements.append(Paragraph(f"{i}. {action}", body_style))

    elements.append(Spacer(1, 0.2 * inch))

    # Strategic
    elements.append(Paragraph("Chiến lược (3-6 Tháng)", subheading_style))
    strategic = data.get("strategic", [
        "Khởi chạy chiến dịch giới thiệu khách hàng (referral program) có thưởng",
        "Xây dựng các cột trụ nội dung (pillar pages) phủ sóng từ khóa ngành lớn",
        "Triển khai chiến dịch quảng cáo tiếp thị lại (retargeting) đa kênh theo phễu",
        "Tối ưu hóa các gói giá dịch vụ dựa trên chỉ số đo lường giá trị thực tế",
    ])
    for i, action in enumerate(strategic, 1):
        elements.append(Paragraph(f"{i}. {action}", body_style))

    elements.append(PageBreak())

    # === COMPETITOR SNAPSHOT ===
    if data.get("competitors"):
        elements.append(Paragraph("Bức tranh Cạnh tranh", heading_style))

        comp_data = [["", data.get("brand_name", "Doanh nghiệp của bạn")] + [comp.get("name", f"Đối thủ {i+1}") for i, comp in enumerate(data["competitors"][:3])]]
        
        comp_rows = ["Positioning", "Pricing", "Social Proof", "Content"]
        comp_rows_vietnamese = {
            "Positioning": "Định vị",
            "Pricing": "Giá cả",
            "Social Proof": "Social Proof",
            "Content": "Nội dung"
        }

        for row_name in comp_rows:
            viet_row_name = comp_rows_vietnamese.get(row_name, row_name)
            row = [viet_row_name, data.get("brand_name", "Doanh nghiệp")]
            for comp in data["competitors"][:3]:
                row.append(comp.get(row_name.lower().replace(" ", "_"), "—"))
            # Ensure consistent columns
            while len(row) < len(comp_data[0]):
                row.append("—")
            comp_data.append(row)

        col_count = len(comp_data[0])
        col_width = 470 / col_count
        comp_table = Table(comp_data, colWidths=[col_width] * col_count)
        comp_table.setStyle(TableStyle([
            ("FONTNAME", (0, 0), (-1, -1), "ArialUnicode"),
            ("BACKGROUND", (0, 0), (-1, 0), COLORS["primary"]),
            ("TEXTCOLOR", (0, 0), (-1, 0), COLORS["white"]),
            ("FONTNAME", (0, 0), (-1, 0), "ArialUnicode-Bold"),
            ("FONTSIZE", (0, 0), (-1, -1), 8),
            ("GRID", (0, 0), (-1, -1), 0.5, COLORS["border"]),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [COLORS["white"], COLORS["light_bg"]]),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING", (0, 0), (-1, -1), 5),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ("FONTNAME", (0, 1), (0, -1), "ArialUnicode-Bold"),
        ]))
        elements.append(comp_table)
        elements.append(PageBreak())

    # === METHODOLOGY ===
    elements.append(Paragraph("Phương pháp đánh giá", heading_style))
    elements.append(Paragraph(
        "Bản đánh giá này đo lường sáu danh mục cốt lõi của hiệu quả marketing. "
        "Mỗi danh mục được chấm điểm từ 0-100 dựa trên các tiêu chuẩn ngành và đối thủ cạnh tranh.",
        body_style
    ))

    method_data = [
        ["Danh mục", "Trọng số", "Nội dung đo lường"],
        ["Content & Messaging", "25%", "Chất lượng copy, Value Proposition, tính rõ ràng của tiêu đề, hiệu quả CTA, nhất quán brand voice"],
        ["Conversion Optimization", "20%", "Thiết kế phễu, tối ưu hóa form, social proof, giảm thiểu ma sát chuyển đổi"],
        ["SEO & Discoverability", "20%", "Tối ưu hóa On-page SEO, Technical SEO, cấu trúc nội dung"],
        ["Competitive Positioning", "15%", "Sự khác biệt thị trường, bảng giá, chiến lược so sánh đối thủ"],
        ["Brand & Trust", "10%", "Chất lượng thiết kế, tín hiệu uy tín, chỉ số thẩm quyền thương hiệu"],
        ["Growth & Strategy", "10%", "Chiến lược định giá, các kênh thu hút khách hàng, khả năng giữ chân khách"],
    ]

    method_table = Table(method_data, colWidths=[140, 50, 280])
    method_table.setStyle(TableStyle([
        ("FONTNAME", (0, 0), (-1, -1), "ArialUnicode"),
        ("BACKGROUND", (0, 0), (-1, 0), COLORS["primary"]),
        ("TEXTCOLOR", (0, 0), (-1, 0), COLORS["white"]),
        ("FONTNAME", (0, 0), (-1, 0), "ArialUnicode-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("GRID", (0, 0), (-1, -1), 0.5, COLORS["border"]),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [COLORS["white"], COLORS["light_bg"]]),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    elements.append(method_table)

    elements.append(Spacer(1, 0.5 * inch))
    elements.append(Paragraph(
        "Được tạo bởi Bitsness AI Marketing Suite",
        ParagraphStyle("Footer", parent=body_style, fontSize=8, textColor=COLORS["text_light"])
    ))

    # Build PDF
    doc.build(elements)
    return output_path


def main():
    if len(sys.argv) < 2:
        # Demo mode — generate sample report
        sample_data = {
            "url": "https://example.com",
            "date": datetime.now().strftime("%d/%m/%Y"),
            "overall_score": 62,
            "executive_summary": "Báo cáo này chỉ ra các cơ hội lớn nhằm tăng tỷ lệ chuyển đổi và củng cố vị thế định vị thương hiệu. Trang web hiện có chất lượng nội dung nền tảng tốt nhưng chưa tối ưu các chuyển đổi và khả năng nhận diện đối thủ cạnh tranh.",
            "categories": {
                "Content & Messaging": {"score": 68, "weight": "25%"},
                "Conversion Optimization": {"score": 52, "weight": "20%"},
                "SEO & Discoverability": {"score": 74, "weight": "20%"},
                "Competitive Positioning": {"score": 48, "weight": "15%"},
                "Brand & Trust": {"score": 70, "weight": "10%"},
                "Growth & Strategy": {"score": 55, "weight": "10%"},
            },
            "findings": [
                {"severity": "Critical", "finding": "Tiêu đề trang chủ viết quá chung chung — chưa truyền tải được giá trị cốt lõi đến đối tượng khách hàng mục tiêu"},
                {"severity": "Critical", "finding": "Thiếu vắng các bằng chứng xã hội (Social Proof) như testimonial, đánh giá trên màn hình đầu tiên trang chủ"},
                {"severity": "High", "finding": "Nút CTA chính sử dụng chữ 'Đăng ký ngay' — nên tối ưu thành từ ngữ hướng lợi ích hành động cụ thể"},
                {"severity": "High", "finding": "Trang bảng giá thiếu phần so sánh tính năng và không chủ động xử lý các e ngại về giá của khách"},
                {"severity": "Medium", "finding": "Thiếu các trang so sánh đối đầu trực tiếp đối thủ — đang mất lượng lớn traffic tìm kiếm tự nhiên"},
                {"severity": "Medium", "finding": "Các bài viết chia sẻ kiến thức blog chưa có link nội bộ dẫn dắt khách tìm hiểu sản phẩm dịch vụ"},
                {"severity": "Low", "finding": "Có link liên kết tài khoản MXH ở chân trang nhưng chưa được đồng bộ nội dung thương hiệu"},
            ],
            "quick_wins": [
                "Viết lại tiêu đề trang chủ: 'Chúng tôi giúp doanh nghiệp tăng trưởng' → 'Tăng gấp 3 lần lượng lead chất lượng trong 30 ngày — không cần gọi điện lạnh'",
                "Bổ sung 5 logo khách hàng tiêu biểu lên đầu trang kèm dòng chữ 'Được tin dùng bởi 500+ doanh nghiệp'",
                "Đổi chữ trên nút form từ 'Gửi đi' thành 'Nhận phân tích đánh giá Marketing miễn phí của tôi'",
                "Bổ sung phần testimonial chi tiết chứa tên tuổi, ảnh chân dung thực tế và kết quả đo lường cụ thể",
            ],
            "medium_term": [
                "Xây dựng Landing Page dạng '[Đối thủ] Alternative' cho top 3 đối thủ lớn nhất",
                "Quay 3 video case study phỏng vấn chia sẻ kết quả thực tế của khách hàng",
                "Cài đặt popup bắt giữ khách có ý định thoát trang kèm quà tặng Lead Magnet hữu ích",
                "Lên chuỗi email nuôi dưỡng tự động chăm sóc lead đăng ký mới",
            ],
            "strategic": [
                "Triển khai chiến lược content hub với 10 trang bài viết cột trụ nhắm từ khóa lượng tìm kiếm cao",
                "Thiết lập chương trình giới thiệu nhận quà lan tỏa (referral program)",
                "Chạy các chiến dịch tiếp thị lại (retargeting ads) trên Google và Meta nhắm trúng đối tượng phễu",
                "Tối ưu hóa bảng giá dịch vụ định hướng theo mô hình giá trị sản phẩm đem lại",
            ],
            "competitors": [
                {"name": "Đối thủ A", "positioning": "Hệ thống tất cả trong một", "pricing": "$49-199/tháng", "social_proof": "10K+ người dùng", "content": "Blog hoạt động tích cực"},
                {"name": "Đối thủ B", "positioning": "Nhắm phân khúc doanh nghiệp lớn", "pricing": "Liên hệ báo giá", "social_proof": "Các logo Fortune 500", "content": "Tập trung viết Whitepapers"},
                {"name": "Đối thủ C", "positioning": "Gói giá bình dân tối giản", "pricing": "Miễn phí - $29/tháng", "social_proof": "Đạt 4.8★ trên G2", "content": "Kênh YouTube chia sẻ mẹo"},
            ],
            "brand_name": "Example Co"
        }

        output = "MARKETING-REPORT-sample.pdf"
        generate_report(sample_data, output)
        print(f"Sample report generated: {output}")
        return

    # JSON input mode
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "MARKETING-REPORT.pdf"

    with open(input_file, "r") as f:
        data = json.load(f)

    generate_report(data, output_file)
    print(f"Report generated: {output_file}")


if __name__ == "__main__":
    main()
