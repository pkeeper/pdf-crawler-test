import logging
from pdfx import PDFx, extract_urls, PDFMinerBackend, \
    PDFSyntaxError, PDFInvalidError, TextBackend
from models import Document, CrawledURL


logger = logging.getLogger(__name__)

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
            raise PDFInvalidError("Error: invalid PDF (%s)" % unicode(e))

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
    logger.info("Processing PDF with name: %s" % name)
    pdf = AdaptedPDFx(name, data)
    urls = pdf.get_references_as_dict().get('url', [])
    logger.info("Metadata: %s" % pdf.get_metadata())
    logger.info("URLs found: %s" % urls or "None")

    logger.info("Saving to DB")
    document = Document(name=name)
    document.save()
    logger.info("Created Document object with 'name' attribute: %s" % name)

    for url in urls:
        u, created = CrawledURL.objects.get_or_create(url=url)
        if created:
            logger.info("Created CrawledURL object for URL: %s" % url)
        document.urls.add(u)
        logger.info("CrawledURL object for URL %s linked to Document" % url)

