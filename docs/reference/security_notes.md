risk = threats x vulnerabilities x consequences

security attributes:
	confidentiality: privacy
	integrity: editability
	availability: access, retainment vs. destruction
	possession: ownership
	utility: usefulness
	authenticity: legitimacy

non-repudiation: inability to deny having received/sent message
authentication: verifies identity of user
authorization: upon authentication, what is it allowed to access (permissions)

defense in depth layers:
- prevention
- detection
- recovery

- risk probability alerts for action on each feature given recent exploits
- give hackers' each others' contact information so they only hack each other and it forms a closed trade loop independent of the economy


virus types:
- macro: usually written in platform-independent language, embedded in docs, usually activated on opening document
- stealth: hides modifictions, trick antivirus into accepting intercepted requests to os
- polymorphic: produces variable copies of itself
- self-garbling: modifies its code to avoid identification
- bots: hacked devices under control of a hacker
- worms: spread from one machine to another
- os root kits: usually embedded in os kernel to hide
- firmware kits: embedded in firmware, can do things like reformatting your drive so the os cant be reinstalled
	- persistence means itll survive a reinstall of the os
- trojan horses: executes malicious code while performing legitimate functions
- rat (remote access tool): allow others to access your system remotely
- key logger: tracks key events
- cpu hijackers

attack types:
- drive-by attacks
- script injection/redirection in adware
- adware forces ads
- scareware: makes user think an attack has happened to trigger an action
- potentially unwanted programs: antivirus cant tell if its intentional installation/download
- cross-site-scripting vulnerability

- hybrid encryption uses symmetric algorithm to encrypt data & asymmetric algorithm to encrypt key exchange
- tls, https over tls, & pgp use hybrid encryption
- digital signature is a hash value encrypted private key, protecting from changes after exchange and authenticating sender