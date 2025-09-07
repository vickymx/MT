# 🌍 Multilingual Functional Texts Database  
**XML-Structured Corpus with Dynamic Access via Python & QR Codes**

---

## 📖 About the Project  
This project demonstrates how short **functional texts** (like *Exit*, *No smoking*, or medical instructions) can be:  

✅ Structured in **XML** with morphological annotation  
✅ Processed and validated using **Python**  
✅ Published as a lightweight **web interface**  
✅ Accessed instantly via **QR codes**  

It was created as part of a Master’s thesis in **Computational Linguistics & Internet Technologies** (Sofia University, 2025).  

---

## 🛠️ Tech Stack  
- **XML + DTD** → Structured corpus with annotation  
- **Python** → Data parsing, validation, QR code generation  
- **lxml, pdfplumber, qrcode** → XML handling & automation  
- **HTML + CSS** → Interactive multilingual interface  
- **GitHub Pages** → Free static hosting for demonstration  

---

## 📂 Repository Structure  

```bash
├── data/
│   ├── texts.xml           # Multilingual XML corpus
│   ├── schema.dtd          # DTD definition
│
├── scripts/
│   ├── process_xml.py      # Parse + validate XML
│   ├── generate_qr.py      # Generate QR codes
│
├── web/
│   ├── index.html          # Multilingual interface
│   ├── style.css           # Simple design
│
├── demo/
│   ├── qr_code.png         # Example QR code
│   └── screenshots/        # Interface demo shots
│
└── README.md
