# LibraryProject
# Security Measures

## Settings
- DEBUG: Set to False in production to prevent detailed error pages.
- SECURE_BROWSER_XSS_FILTER: Enabled to prevent XSS attacks.
- X_FRAME_OPTIONS: Set to 'DENY' to prevent clickjacking.
- SECURE_CONTENT_TYPE_NOSNIFF: Enabled to prevent MIME type sniffing.
- CSRF_COOKIE_SECURE: Ensures CSRF cookies are sent over HTTPS only.
- SESSION_COOKIE_SECURE: Ensures session cookies are sent over HTTPS only.

## CSRF Protection
- All forms include the {% csrf_token %} tag to protect against CSRF attacks.

## Data Access
- Used Django’s ORM to parameterize queries and avoid SQL injection.
- Validated and sanitized user inputs using Django forms.

## Content Security Policy (CSP)
- Configured CSP to reduce the risk of XSS attacks by specifying trusted sources for content.