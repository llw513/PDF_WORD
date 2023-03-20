import pdfplumber
from docx import Document

# 读取PDF文件
with pdfplumber.open('example.pdf') as pdf_file:
    # 创建空白Word文档
    document = Document()
    
    # 循环读取PDF中的每一页
    for page in pdf_file.pages:
        # 将PDF页转换为文本
        text = page.extract_text()
        print(text)
        # 如果文本不为空，则将文本添加到Word文档中
        if text:
            document.add_paragraph(text)
    
    # 将Word文档保存为docx格式
    document.save('example.docx')
