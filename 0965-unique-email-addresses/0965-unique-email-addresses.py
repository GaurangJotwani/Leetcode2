class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        unique_emails = set()

        for email in emails:
            unique_emails.add(self.emailParser(email))
        
        return len(unique_emails)
    
    def emailParser(self, email):

        local, domain = email.split("@")
        parsed = []

        for char in local:
            if char == "+":
                break
            if char == ".":
                continue
            parsed.append(char)
        
        new_email = "".join(parsed) + "@" + domain
        return new_email
    

        