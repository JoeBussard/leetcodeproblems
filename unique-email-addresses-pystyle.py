
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
#       def remove_plus_sign_suffix(localname):
#           if "+" in localname:
#               return localname[:localname.index("+")]
#           return localname
#       
#       def split_local_name_and_domain_name(email):
#           if '@' in email:
#               localname = email[:email.index('@')]
#               domainname = email[email.index('@')+1:]
#               return localname, domainname
#           else:
#               print("Your email address is bogus")
#               return None, None
#       
#       def ignore_dot_in_local_name(localname):
#           new_name = localname
#           while '.' in new_name:
#               new_name = new_name[:new_name.index('.')] + new_name[new_name.index('.')+1:]
#           return new_name 

      legit_emails = []
      for email in emails:
          localname, domainname = split_local_name_and_domain_name(email)
          localname = remove_plus_sign_suffix(localname)
          localname = ignore_dot_in_local_name(localname)
          legit_email =str(localname + '@' + domainname)
          if legit_email not in legit_emails:
              print(legit_email, "is a legit email")
              legit_emails.append(legit_email)
          else:
              print(legit_email, "already exists in")
              print(legit_emails)
      return len(legit_emails)

          

