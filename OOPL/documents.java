public class ConfidentialDocument implements Cloneable {
    private String title;
    private String content;
    private String securityLevel;

    public ConfidentialDocument(String title, String content, String securityLevel) {
        this.title = title;
        this.content = content;
        this.securityLevel = securityLevel;
    }

    public String getTitle() {
        return title;
    }

    public String getContent() {
        return content;
    }

    public String getSecurityLevel() {
        return securityLevel;
    }

    public void setContent(String content) {
        this.content = content;
    }

    @Override
    public ConfidentialDocument clone() {
        try {
            ConfidentialDocument clonedDocument = (ConfidentialDocument) super.clone();
            clonedDocument.securityLevel = "Default";
            return clonedDocument;
        } catch (CloneNotSupportedException e) {
            throw new AssertionError(e);
        }
    }

    public static void main(String[] args) {
        ConfidentialDocument originalDocument = new ConfidentialDocument("Secret Report", "Confidential information", "High");
        ConfidentialDocument clonedDocument = originalDocument.clone();
        clonedDocument.setContent("Updated content");

        System.out.println("Original Document:");
        displayDocumentDetails(originalDocument);

        System.out.println("\nCloned Document:");
        displayDocumentDetails(clonedDocument);
    }

    public static void displayDocumentDetails(ConfidentialDocument document) {
        System.out.println("Title: " + document.getTitle());
        System.out.println("Content: " + document.getContent());
        System.out.println("Security Level: " + document.getSecurityLevel());
    }
}
