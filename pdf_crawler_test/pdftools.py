import logging
from pdfx import PDFx, extract_urls, PDFMinerBackend, \
    PDFSyntaxError, PDFInvalidError, TextBackend


logger = logging.getLogger()

class AdaptedPDFx (PDFx):
    def __init__(self, name, stream):
        """
        Open PDF handle and parse PDF metadata
        """
        self.fn = name
        self.stream = stream


        # Create ReaderBackend instance
        try:
            self.reader = PDFMinerBackend(self.stream)
        except PDFSyntaxError as e:
            # Could try to create a TextReader
            try:
                logger.info(unicode(e))
                logger.info("Trying to create a TextReader backend...")
                self.stream.seek(0)
                self.reader = TextBackend(self.stream)
                self.is_pdf = False
            except Exception as e:
                raise PDFInvalidError("Invalid PDF (%s)" % unicode(e))


        # Save metadata to user-supplied directory
        self.summary = {
            "filename": self.fn,
            "metadata": self.reader.get_metadata(),
        }

        # Search for URLs
        self.summary["references"] = self.reader.get_references_as_dict()
        # print(self.summary)

def handle_pdf(name, data):
    # Read PDF and return URL's list
    pdf = AdaptedPDFx(name, data)
    print ("Metadata: ", pdf.get_metadata())
    print ("references_list", pdf.get_references())
    print ("references_dict", pdf.get_references_as_dict())
