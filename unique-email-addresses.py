class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
      legit_emails = set()

      for email in emails:
          localname, domainname = email.split('@')
          localname = localname.replace('.', '')
          localname = localname.split("+")[0]
          legit_emails.add(localname + '@' + domainname)
      return len(legit_emails)
