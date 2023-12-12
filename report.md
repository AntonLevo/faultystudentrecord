*This vulnerability report template is offered to you by the GitHub Security Lab. Use it as an inspiration for your own reports. Reporting a vulnerability using this template does not imply that this report has been acknowledged by the GitHub Security Lab. Remove this first section and any mention of the GitHub Security Lab when you use this template.* 

# Vulnerability Report

I identified potential security vulnerabilities in faulty student records.

I am committed to working with you to help resolve these issues. In this report, you will find everything you need to effectively coordinate a resolution of these issues.

If at any point you have concerns or questions about this process, please do not hesitate to reach out to me at anton.levo@student.laurea.fi.

If you are _NOT_ the correct point of contact for this report, please let me know!

## Summary

The faulty student record system contains several security vulnerabilities such as;  SQL injection, plain text password storage, and inadequate file upload security. These vulnerabilities could lead to unauthorized access, data manipulation, and compromise of sensitive information.

## Product

Student Record System

## Details

# 1. SQL-injection vulnerability
in the "login()" (Row 47) function there is no validation in the SQL queries done allowing an attacker to exploit the system by changing the queries.

# 2. Passwords saved on a text file
The file to store the passwords is a plain text file without any form of encryption. Anyone having access to the file could read it externally in any application. This could be fixed by implementing a hashing algorithm to secure the passwords.

# 3. Lacking security considerations in the file upload 
There is no proper validation or sanitization for file uploads. File size limiting is important to implement to avoid attacks through unwanted file types or sizes.

# 4. No session management
The code doesn't handle user sessions well. After someone logs in successfully, there's no setup for secure session management using tokens or cookies. Proper management can help to stop others from taking over a session for unauthorized access.
# 5. No HTTPS
In an online deployment, there is no HTTPS encryption in the transmission between client and server.

# 6. Lack of 2FA
There is no support for two-factor authentication, if this was deployed in a cloud-based solution. This could lead to user accounts getting stolen. 

# 7. Limited password policy
There are no requirements for the level of the passwords. A password requirement policy would reduce the risk of password-related attacks.

There are also no fallbacks for brute-force attacks. 

# 8. Insecure Input Handling
The code doesn't check or clean up the information in the user's typing fields. This leaves a possibility for errors if the program doesn't recognize the inputs or worse, leads to malicious code being injected granting potential access to the system. 

# 9. Potential Information Disclosure
Once a student's picture is downloaded, this code allows the user to see the filename and metadata potentially exposing personal information. (such as location tags etc.)


## PoC

*Complete instructions, including specific configuration details, to reproduce the vulnerability*

## Impact

[Impact]

## Remediation

# 1. SQL injection vulnerability
To address this vulnerability, implementing parameterized queries should help...
### cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))

# 2. Storing passwords with a hashing algorithm
### import bcrypt 

hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# 3. File upload size policy

### allowed_extensions = ['jpg', 'jpeg', 'png', 'pdf']
if not file_name.lower().endswith(tuple(allowed_extensions)):
### max_file_size = 5 * 1024 * 1024  # 5 MB in bytes

# 4. Session management
Session management could be dealt with by implementing the use of tokens or cookies with the login. For example, the Flask-Session extension can be used on a server-side session to store data.

# 5. HTTPS
An SSL certificate for the domain in an online deployment will be crucial for protecting the data transmitted between the user and server. Some certificates may cost and some may be free to implement. 

## GitHub Security Advisories

If possible, please could you create a private [GitHub Security Advisory](https://help.github.com/en/github/managing-security-vulnerabilities/creating-a-security-advisory) for these findings? This allows you to invite me to collaborate and further discuss these findings in private before they are [published](https://help.github.com/en/github/managing-security-vulnerabilities/publishing-a-security-advisory). I will be happy to collaborate with you, and review your fix to make sure that all corner cases are covered. 
When you use a GitHub Security Advisory, you can request a CVE identification number from GitHub. GitHub usually reviews the request within 72 hours, and the CVE details will be published after you make your security advisory public. Publishing a GitHub Security Advisory and a CVE will help notify the downstream consumers of your project, so they can update to the fixed version.

## Credit

*List all researchers who contributed to this disclosure.*
*If you found the vulnerability with a specific tool, you can also credit this tool.*

## Contact

anton.levo@student.laurea.fi

## Disclosure Policy

*Describe or link to your disclosure policy. It's important to have a disclosure policy where the public disclosure deadline, and the potential exceptions to it, are clear. You are free to use the [GitHub Security Lab disclosure policy](https://securitylab.github.com/advisories/#policy), which is copied below for your convenience if it resonates with you.*

The *your_team_name_here* research team is dedicated to working closely with the open-source community and with projects that are affected by a vulnerability, to protect users and ensure a coordinated disclosure. When we identify a vulnerability in a project, we will report it by contacting the publicly listed security contact for the project if one exists; otherwise, we will attempt to contact the project maintainers directly.

If the project team responds and agrees the issue poses a security risk, we will work with the project security team or maintainers to communicate the vulnerability in detail and agree on the process for public disclosure. Responsibility for developing and releasing a patch lies firmly with the project team, though we aim to facilitate this by providing detailed information about the vulnerability.

Our disclosure deadline for publicly disclosing a vulnerability is: 90 days after the first report to the project team.

We **appreciate the hard work** maintainers put into fixing vulnerabilities and understand that sometimes more time is required to properly address an issue. We want project maintainers to succeed and because of that, we are always open to discuss our disclosure policy to fit your specific requirements, when warranted.
