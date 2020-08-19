- to do:

	- finish es import function for other data, config elk stack for ml anomaly detection & test

	- finish scaling in preprocessing

	- add regularization/normalization

	- finish deploy functions in deploy.py

	- finish install scripts

		- xgboost installation
			brew install cmake && gcc@8
			git clone --recursive https://github.com/dmlc/xgboost && mkdir xgboost/my_build && cd xgboost/my_build
			CC=gcc-8 CXX=g++-8 cmake ..
			make -j4
			cd ../python_package && python3 setup.py install

			git clone --recursive https://github.com/dmlc/xgboost
			cd xgboost
			cp make/minimum.mk ./config.mk
			make -j4
			cd python-package
			sudo python setup.py install

	- finish metric graph function & data set graph function with hover tooltip

	- create deployed instances to test

	- function to pull data from es with label column parameter & apply a standard model & output metric graph

	- label data & train

	- email metadata identification functions

	- label some example data & data from the email data set with metadata (semantic like assumptions, structural like keywords)

		- example: 'Clarence told me that x'

			- assumptions
				- assumption: 'that you know who Clarence is'
					- assumption reason: 'because they didnt include the last name'
					- assumption type: 'you know the missing information'

				- assumption: 'that you want to know who gave me the information' (hence why theyre telling you)
					- assumption reason: 'because its not certain that you need/want to know who gave you the information, as there may be protocols involved precluding that'
					- assumption type: assuming intent (assuming you intend to find out who gave them the information)
			
			- implications
				- 'they had a conversation with Clarence' (implies conversation object)
				- 'Clarence had valuable information to communicate' (implies valuable information exchange potential & execution)
				- 'Clarence thought it was best/important/necessary to communicate this to recipients' (implies reason for the communication)
			
			- questions
				- situation context: 'was the conversation in a meeting or in private'
				- medium: 'was the conversation by email/chat/phone, in person, or by video conference'
			
			- intents
				- direct intents
					- 'indicate the source of information' (add legitimacy or deflect responsibility)
					- 'indicate that they have information x' (prepare the recipient)
					- 'indicate that they would like to share this information x with you' (explicitly/implicitly declare their intent)
					- 'indicate information x' (share information)

				- alternative intents
					- 'Clarence did not intend to send this (or some email metadata like recipient or timing or content was accidental)' (explanation for irrelevant information)
					- 'Clarence did not finish the email' (explanation for incompleteness)
					- 'Clarence did not organize/format the email, swayed by his emotional state or imminent deadline' (explanation for disorganization)
					- 'Clarence forgot he already sent this email or a similar email' (explanation for repetition)
					- 'Clarence or his source was misinformed' (explanation for misinformation)
					- 'Clarence is trying to be deceptive' (explanation for misinformation)
					- 'Clarence forgot to take out information y' (explanation for excessive information)

	- apply semantic model with schema identification & logic functions

	- document multiple elk stacks for applied filters (legit email addresses, matching legit templates, matching anomaly patterns)

	- a requirement of the assumption/intent/implication model is:
		- a network of objects inherent to the problem space
		- a set of queries for each object type to fetch the related objects
			- query to get surrounding objects to retrieve implications of a statement (node connection)
			- query to get requirements + prior implications to retrieve assumptions of a statement (node connection)
			- query to get paths using a node to get intents for a statement (node connection)
			- query to get missing information & uncertainty structures to get questions for a statement (node connection)

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

	- query patterns in language map graph database queries

		- assumption
			- subset of a set (missing information generating assumption being the subset)
			- context mismatch (applying an unproven statement as a fact, rather than applying tests to prove it)

		- implication
			- structures with related required or probable structures (preceding input/following output, application intent, containing context, possibility/requirement, disabling/enabling, competing exclusive/coordinating inclusive)

		- intent
			- output
				- intended/expected/supported function output
				- function side effects
					- side effects of calling the function (using/accessing memory, applying an inefficiency of that function)
					- side effects of using/producing inputs/outputs (locking input data so it cant be simultaneous accessed by some process)
					- side effects of outputs (non-randomness coincidentally appearing in random set likelier to be guessed first)
					- side effects of input-output pairs (favoring a pre-computation, input/output pair, or other assumption, or traversing a particular network route or function set)

		- question
			- structural:
				- how: path involving alternatives that need to be resolved
					- how to get from origin to target
 
			- semantic:
				- why: path moving in a priority direction or having a causal metadata attribute value (structure, degree, power)
					- why to aim for target or start at origin
					- what priority direction does trajectory align with, generate, or use?
					- what is the causal structure (origin) of target

- functions to build

	- standardize words in a document

	- identify email metadata

		- category by ml/regex model (business, admin, small talk, etc)
		- topic (security, incident, meeting, etc)
		- summary
		- intent by ml/regex model (transfer knowlege, ask question, introduce people, etc)
			- intent metadata (sequence, degree of sentiments, determination to complete intent, method of applying intent, assumption/implication of intent)
		- context (approved/legitimate object/function/attribute) fit (is there actually a meeting/document as mentioned in the email? did they use real names of coworkers? did they use full name or actual used name?)

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

		- related objects (emails)

	- measure how similar two documents are (for comparing email to standard email for an intent, or malicious emails)
		- tf-idf cosine similarity
		- levenshtein distance between strings
		- shannon entropy for detecting random (as a proxy for auto-generated) strings
		- trajectory across language map
		- fit of document to approved object relationship network (network of relationships between approved objects like contacts in the company, services, tools we use, etc)
		- word frequency for email metadata (email type, intent, email variation)

	- combine features in structures like conditions/sequences (x given y)

	- format features (position/trajectory in approved object network) to train ml models on, bc algorithms cant infer all those objects

	- identify what relationships & relationship structures are significant in identifying attacks

		- attack : attack structure (sequence, network)
			- is this attack a distortion of previous attacks (is the attacker learning or inventing new attack vectors or developing an attack model in a standard way)

		- distortion vectors (conversion vectors from official to casual content): attributes produced by distortions (casual tone)

		- info : info object type (as a proxy for info object definition/identification function, keyword counting, templates, or regex)

		- variable interaction space for building a model for model performance & vertex identification

			- variables
			- variable layers
				- value-differentiating rules
					- variable size, like number of words or the grouping rule used to categorize values for a variable, like the rule differentiating word vs. phrase vs. sentence)
						- example grouping mechanism other than size
							- phrases have adjacence to/containment by filler words or identifying words like subjects & subject action verbs
							- sentences have subject-predicate clauses
						- sentence: sentence
							- is this sentence normal for its contexts (neighbors, summary, paragraph, template, email title/subject/recipients/metadata)
						- sentence: word (is the word normal for this sentence, is the sentence normal for this word
				- variable-grouping rules (into types, relevant variable sets, isolatable variable sets, alternative or proxy sets, outlier-predicting sets, etc)
			- probability distribution for variables
				- there will occasionally be a need for an outlier variable to make certain predictions, resolving questions that dont come up often
				- common variable sets can be pulled from variables within x standard deviations away (variable sets which may have the same/similar average or average definition)
			- variable sequences (ordered by importance, causal direction, etc)
			- variable combinations (functions relevant to the prediction function, like adjacent/subset/component or moment/probability distribution functions)
			- variable circuits/trees/networks
			- vertexes: positions in variable interaction space where navigating away from vertex variable set reduces accuracy of prediction
				- can be in the generative interaction space or in the existing interaction space variable structures
				- can indicate a relevant format/base/structure
				- can identify/infer relevant missing information, like a system context

		- data set: predicted label

			- email:
				- email: category (topic, error type, attack type)
					- is this email normal for this category
				- email: info objects (assumption, implication, intent, question, missing information, format, requirement, logical jump, conclusion, inference, fact, insight)
					- insights are important to identify for alerting purposes (new important information that explains a system should be prioritized)

			- standardized & metadata versions of the above
				- standardized sentence: standardized word
				- sentence metadata: word metadata

			- asymmetries: which variables are better predictors than predicted given causal position, required intent, and ability to lose information for that intent

				- if we have surrounding (preceding/alternative/following) variables for a target variable in a causal structure, can we infer the surrounded target variable (and its metadata if not provided) with the other surrounding variable data, with a model of sub-systems that could be determining that variable, if its complexity is variable)
					- like how 'level of variation from template' is an interim variable, predicted by email/template metadata, & predicting the output attack type
					- certain types of these surrounded/interim variables will be inferable, even with overlap across type values, and even with missing variables
					- the reason for inferring the surrounded 'level of variation' variable in the data missing it is to use it as a predictor in data including it

				- other variable relationships involve loss of information in one direction, depending on context
					- type data can lose information in a context with multiple different classes having significant differences, but having the same type, if the type is too general
					- type information should be stored at the right abstraction level for intent
						- storing a species variant rather than a species can be:
							- an information loss, including type-conflation examples like:
								- comparing chihuahuas to cats loses the information that other dogs are similar/different to cats in various ways, like:
									- cats that bark (over-focuses on type, rather than the important variable, which is proximity within types likely to be domesticated both having vocal chords with structural similarities necessary for audio data misidentifications)
									- dwarf dogs with similar sizes to cats (there are other similarities that can produce misidentifications in image data)
									- dogs with mutations (one-population type distortions) that make them seem similar to chihuahuas or cats
							- an information gain
								- comparing chihuahuas to cats highlights the significant similarities between them that are more relevant to certain question than comparing all dogs to cats, like intent to resolve misidentification problem types
					- this requires identifying limiting rules of cause (rules that aggregate cause, allocate cause, or route cause in a direction)

		- definition of metric:

			- what definition of normal (normal across all data, normal for a sub-type, normal for a metadata set)
			- what other metrics are used instead of average
				- within expected/supported variation
				- within variation indicating a change state
				- within outlier variation
				- within range predicted for noise ratio
				- distance from random/other bases

		- mixed relationships across above variable variables, with math metrics describing them

			- '3 word-sentence anomalies in different paragraphs compared to their positions in the primary intent summary'
			- '5:2 ratio of topic-assumption anomalies in email, compared to email template'

		- type conflation routes 

			- how one type can appear to be another type, with a false (chihuahua is not a cat) or semi-relevant similarity (noises may be similarly possible across types bc of similar vocal chords, which may differ within/across types given sub-species and mutations, helping differentiate the types

	- identify info structure definitions


- schema

	- security objects

		- attack 
			- types
			- patterns
			- templates

		- error 
			- types
			- patterns
			- templates

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

	- info objects

		- summary

			- includes insights, abstract summary using metadata, quick summary (communicates general intent while losing information like tone, or identifies best reason to read the document, or summarizes relevant objects like primary argument or set of strategies/fallacies used, or missing information)

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

			- structures:
				- assumptions can be found in contradictions
					- example: a statement implying an exclusive/certain path (related species has X, so they must have co-evolved it on the same lineage before splitting), when a contradictory alternate possible path was mentioned (independently evolving it), and the reason for certainty/exclusivity wasnt given (why could it not be independently evolved)

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
				- point (theres a reason for x, and the reason is y, so x can be used in structures requiring y)
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
					- email
						- notify about a meeting
						- send follow-up to a meeting
						- recommend reading a policy or document
						- share work-related information necessary to perform job well
						- reset password
					- web
						- check email
						- check dashboard/alerts/reports
						- download data for local work

				- unapproved intents:
					- request sensitive data (account numbers/passwords)
					- get resource (permission, event)
					- access memory/script
					- edit/inject/install code
					- direct memory retrieval

			- missing information for a given intent, mismatches between email structure/content and stated intent, distortions that aren't composable with approved core functions
		
		- question
			- definition: implied trajectory between source/target
			- types:
				- structural question: a question of how to connect source/target, source/target metadata (identity/position)
				- semantic question: a question of why to connect source/target
					- cause question: a question of which causal structure/layer/degree/power is relevant
					- reason question: a question of emergent intent (what priority does this fulfill or rule out eventually)
				 
		- expectations
			- users will stick to approved intents
			- sometimes users will want freedom from approved intents
			- users tend to use decision functions that have patterns
			- requests/events that differs from expectations (approved intents) need to have a reason justifying the distortion, from a set of approved distortion reasons

		- system objects
			- filters (filters for suspicious data, filters for access)
			- injection points, false similarities/alignments, distortions, & distortion patterns


- data
	- incidents
	- email data set
		- https://spamassassin.apache.org/old/publiccorpus/
		- https://www.kaggle.com/rtatman/fraudulent-email-corpus?select=fradulent_emails.txt
	- event data access (browser history data can be used for inferring legitimacy of requested actions like clicking password reset link)

- ai/security cloud tools
	- ai models/regex patterns
