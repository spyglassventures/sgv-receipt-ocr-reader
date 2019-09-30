## learn how to NLTK
# more Rest API
# sentiment
# OCR from pictures, put in list, LIDL
# learn Docker
# Kibana dashboard


brew install tesseract --with-all-languages
ocrmypdf - l  de IMG0001.jpg LeParisien.pdf



tesseract IMG0001.jpg output-prefix pdf
ocrmypdf --sidecar output.txt IMG0001.jpg output.pdf # geht nicht
ocrmypdf -l deu --sidecar output.txt IMG_1052.HEIC.pdf output.pdf
ocrmypdf --sidecar output.txt IMG_1052.HEIC.pdf output.pdf


# Language German
https://www.heise.de/ct/artikel/Toolbox-Texterkennung-mit-OCRmyPDF-2356670.html


# as PDF
ocrmypdf --sidecar output_eng.txt Lidl_Rechnung.pdf output.pdf
ocrmypdf -l deu --sidecar output_german.txt Lidl_Rechnung.pdf output.pdf


# as JPG
ocrmypdf --sidecar output_eng.txt Lidl_Rechnung.jpg output.pdf
ocrmypdf -l deu --sidecar output_german.txt Lidl_Rechnung.jpg output.pdf

# as PDF
ocrmypdf --sidecar output_eng.txt IMG_1057.HEIC.pdf output_LIDL.pdf
ocrmypdf -l deu --sidecar output_german.txt IMG_1057.HEIC.pdf output_LIDL.pdf


## Evaluation Exp1: Input File 72 MB = works
ocrmypdf --sidecar output_eng.txt IMG_1057.HEIC.pdf output_LIDL.pdf
ocrmypdf -l deu --sidecar output_ger.txt IMG_1057.HEIC.pdf output_LIDL.pdf


## Evaluation Exp2: Input File - output = none
ocrmypdf --sidecar output_eng.txt Lidl_Rechnung.jpg output_LIDL.pdf
ocrmypdf -l deu --sidecar output_ger.txt Lidl_Rechung.jpeg output_LIDL.pdf


## Evaluation Exp3: Input File - output = none
ocrmypdf --sidecar output_eng.txt Lidl_Rechnung_jpg2pdf.pdf output_LIDL.pdf
ocrmypdf -l deu --sidecar output_ger.txt Lidl_Rechnung_jpg2pdf.pdf output_LIDL.pdf


## Evaluation Exp4: file from Exp1, but exported as jpg with highest quality, numbers are lost?
ocrmypdf --sidecar output_eng.txt IMG_1057.jpg output_LIDL.pdf
ocrmypdf -l deu --sidecar output_ger.txt IMG_1057.jpg output_LIDL.pdf


## Evaluation Exp5: file from Exp4, but with cut borders
ocrmypdf --sidecar output_eng.txt IMG_1057.jpg output_LIDL.pdf
ocrmypdf -l deu --sidecar output_ger.txt IMG_1057.jpg output_LIDL.pdf