- to do:
	- label some example data & data from the email data set (aim for 100-200 records)
	- train algorithm that works with small data sets until you can import more
	- spin up elk stack
	- import email data set to elk stack
	- create wrappers for api queries
	- test algorithm on untrained email 

	- data examples

		- example: 'Clarence told me that x'

			- assumptions:
				- assumption: 'you know who Clarence is'
					- assumption reason: 'because they didnt include the last name'
					- assumption type: 'you know the missing information'

				- assumption: 'you want to know who gave me the information' (hence why theyre telling you)
					- assumption reason: 'because its not certain that you need/want to know who gave you the information, as there may be protocols involved precluding that'
					- assumption type: assuming intent (assuming you intend to find out who gave them the information)
			
			- implications
				- 'they had a conversation with Clarence'
				- 'Clarence had valuable information to communicate'
				- 'Clarence thought it was best to communicate this to them'
			
			- questions
				- 'was the conversation in a meeting or in private'
				- 'was the conversation by email/chat/phone, in person, or by video conference'
			
			- intents
				- 'indicate the source of information' (Clarence)
				- 'indicate that they have information x'
				- 'indicate that they would like to share this information x with you'


	- regex model for language patterns

		- assumption (unproven statement)
			- keywords: required/necessary/given/if/since/as/while/though/however/but/then/condition/assuming
			- context: 
				- usually preceding a recommendation
				- all information has assumptions, such as assumptions about:
					- information content, like that the email content is true/relevant
					- information metadata, like that the recipient list is accurate, information format is correct, information context is appropriate
		
		- implication (unclear but nonzero signal)
			- keywords: previously/prior/imminent/future/follows/logically/because/implied/implying/indicating/signaling
			- context:
				- usually not stated
				- have to be inferred with common interaction patterns/rules
				- involve a connection to an object in the origin statement (inferring the 'cat did something' from the origin statement 'dog chases cat' is connected by the cat object)

		- intent (justifiable usage)
			- keywords: because/for/for purposes of/in order to/(to get/accomplish)/so that/to enable/(for/with reason(s/ing))
			- context:
				- usually used to connect origin & target states/positions, since intents are a parallel object to functions

		- question
			- keywords: whether/if/regardless/respective/in relation to/depending on (contextual information is dependent on other information that may not be known yet)
			- context:
				- each assumption has an implied question (is the assumption true/relevant/appropriate to apply in the 'fact' position)
				- each implication has questions of implied relevance (is the implication relevant, does it fit other info)

	- semantic model:

		- communication
			- types
				- email to draw attention to something (reminder of deadline)
				- email for reference (legal policy)
				- email to share immediately useful information (in various formats, like document link or password reset link)
			- contexts
				- user configurations (spam model action history, email folder/action routing configurations)
				- user email history (user typically does a particular action on similarly impersonal/styled/official looking emails)
				- user web history (user just requested a password reset)
				- user expectations (user expects important information to be styled or communicated a certain way)
			- attributes
				- legitimacy
					- template compliance (how much does this email comply with the template for the email type or other metadata)
					- impersonality (how specific is the email to the user)
					- relevance (how much does the user need this information)
					- expectation
						- is the email expected
							- does it occur regularly (meeting reminder)
							- is it something the user configured or intentionally triggered (scheduled alarm or incident level alarm)
							- is it a normal communication about their work (an email about a follow-up meeting to a meeting just completed)
						- what does the email sender expect in response
			- function
				- communicates information successfully, clearly, relevantly, efficiently

		- assumption
			- types:
				- unproven declarative statements (may include facts, but are assumed true even if not)
				- assumption of recipient:
					- information (already know missing implied information not provided)
					- intent (example: want to know relevant communicated information)
					- permission (authority to know)
					- function (ability to know, responsibility to know)
				- uses an unproven statement in an inappropriate fact context (assumes an unproven statement to be true)

		- implication
			- information revealed about system context
				- to do: train a separate algorithm to infer system context from implication data & vice versa)
			- infer implied prior/future events from a statement
				- from the origin statement 'dog chases cat', you can infer:
					- 'the cat did something'
						- implies that 'the cat can do something to trigger the chasing function' and 'the dog reacts to certain stressors with chasing'
					- 'the dog has a chasing function activated by default when theyre not doing other things'
						- implies that 'the dog was not doing other things' and the 'cat did not do something to trigger it'
			- types: 
				- past tense (event y, bc connected event x with y output already happened)
				- future tense (event y, so connected event z with y input will happen)
				- possibility (event x, so system where x is possible or where x can develop)
				- necessity (x, so inputs/requirement of or foundation enabling x)
				- coincidence (x is something that just happens sometimes from lack of distractions 'dog was bored & chasing negates boredom' or happened because of a different trigger, creating a false similarity 'dog was chasing other cat and appeared to be chasing original cat', or is configured by default 'dog just chases things by default')
				- related objects
					- function metadata
						- input/output (event x origin, so connected event y origin)
						- types (event x type, so connected event y type)
						- intents (x, by intent c is reasonable in that context)

		- intent	

			- definition: reason to use a function (choose a word, imply/assume/state something)
				- intent implies agency/choice, so accidental connections are important to identify as unlikely to be an intent

			- types:

				- general intents
					- communicate (communicate info, communicate info metadata like source)

				- neutral intents
					- obfuscate ('someone told me' to protect Clarence from scrutiny, or to hide illegally obtained information)
					- check (ask a question to test/verify/check)

				- approved intents:
					- notify about a meeting
					- send follow-up to a meeting
					- recommend reading a policy or document
					- share work-related information necessary to perform job well
					- reset password

				- unapproved intents:
					- request sensitive data (account numbers/passwords)


		- question

	- query patterns in language map graph database queries
		- assumption

		- implication

		- intent

		- question


- functions

	- standardize words in a document

	- email metadata

		- category by ml/regex model (business, admin, small talk, etc)
		- topic (security, incident, meeting, etc)
		- summary

		- intent by ml/regex model (transfer knowlege, ask question, introduce people, etc)
			- intent metadata (sequence, degree of sentiments, determination to complete intent, method of applying intent, assumption/implication of intent)

		- approved/legitimate object/function/attribute fit (is there actually a meeting/document as mentioned in the email? did they use real names of coworkers? did they use full name or actual used name?)

		- variation
			- how many different intents/problems/questions mentioned
			- differences in sentence metadata (sequence, format, word choice given the rest of the sentence/email, grammar)
			- differences in word metadata (word choice)
			- variation from user-specific style/language (is this person a good communicator, are they learning english, do they prefer email to communicate, etc)

		- exploit objects
			- assumptions (assume that youre the right person to receive the email)
				- expectations (expect that you know the person/process/tool referenced in the email)
			- implications (imply that the email is internal, imply that you need to reset your password, imply that you need to click a link)
			- unenforced rules (does expectation or assumption match intent? is it supposed to differ from intent?)
				- mismatches (does email/headers/content match the implication that its internal, did you try to reset your password)

		- related emails

	- measure how similar two documents are (for comparing email to standard email for an intent, or malicious emails)
		- tf-idf cosine similarity
		- trajectory across language map
		- fit of document to approved object relationship network (network of relationships between approved objects like contacts in the company, services, tools we use, etc)
		- word frequency for email metadata (email type, intent, email variation)

	- combine features in structures like conditions/sequences (x given y)
	- format features (position/trajectory in approved object network) to train ml models on bc algorithms cant infer all those objects

- data
	- incidents
	- email data set
	- event data access (browser history data can be used for inferring legitimacy of requested actions like clicking password reset link)

- ai/security cloud tools

- ai models

- regex patterns

- attack 
	- types
	- patterns
	- templates

- error 
	- types
	- patterns
	- templates

- info objects

	- intent
		- approved intents
			- check email
			- check dashboard/alerts/reports
			- download data for local work

		- malicious intents
			- get resource (permission, event)
			- access memory/script
			- edit/inject/install code
			- direct memory retrieval

		- missing information for a given intent, mismatches between email structure/content and stated intent, distortions that aren't composable with approved core functions
	
	- expectations
		- users will stick to approved intents
		- sometimes users will want freedom from approved intents
		- users tend to use decision functions that have patterns
		- requests/events that differs from expectations (approved intents) need to have a reason justifying the distortion, from a set of approved distortion reasons

- system objects
	- filters (filters for suspicious data, filters for access)
	- injection points, false similarities/alignments, distortions, & distortion patterns

- privilege objects
	- sensitive information
	- permissions
	- access-granting protocol
	- user types

- resource access objects
	- tools
	- implementations
	- versions
	- dependencies
	- events
	- use cases (need to know)

- methods