import pdfplumber
import re

ss_pdf_columns = ["DivisionName", "StockistName", "ProductName", "FreeStrips", "OpeningQty",
                  "PurchaseQty",
                  "SalesQty", "ClosingQty", "Date"]

pw_pdf_columns = ["DivisionName", "StockistName", "ChemistName", "ProductName", "FreeStrip", "SellStrip",
                  "ExpiredQty", "ReturnQty", "DamageQty", "Rate", "Date"]


def extract_text(cls):
    with pdfplumber.open(cls.file) as pdf:
        for page in pdf.pages:
            cls.text += page.extract_text()


def remove_unnecessary_space(cls):
    pattern = r'^[-\s]+$'
    cls.text = re.sub(pattern, '', cls.text, flags=re.MULTILINE)
