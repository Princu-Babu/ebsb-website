# Security Policy

## Supported Versions

Since this is a static website (HTML, CSS, JS) with no backend logic, database, or server-side data processing, the attack surface is extremely minimal. 

| Version | Supported          |
| ------- | ------------------ |
| Latest  | :white_check_mark: |

## Site Security Features
- **Static Content**: The site is 100% static. There are no databases to perform SQL injections on.
- **No Backend**: There is no server logic, meaning Remote Code Execution (RCE) vulnerabilities are not applicable.
- **Client-side only**: All JavaScript runs purely on the client side without handling sensitive user data or authentication tokens.

## Reporting a Vulnerability

If you discover a potential vulnerability or if a third-party CDN link becomes compromised, please report it to the EBSB IT team or the repository maintainer immediately.

Do not create a public issue for severe security vulnerabilities. Please email the maintainers directly.
