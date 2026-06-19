# questions_data.py

def get_questions_for_course(course_name, course_id):

    if course_name == "Python Programming":
        return [
            (course_id, "What is Python?", "Programming Language", "Database", "Browser", "OS", 1),
            (course_id, "Which keyword defines a function?", "func", "define", "def", "function", 3),
            (course_id, "Which data type is immutable?", "List", "Dictionary", "Set", "Tuple", 4),
            (course_id, "What is used for comments?", "//", "#", "/* */", "--", 2),
            (course_id, "Which is a Python web framework?", "Flask", "React", "Angular", "Vue", 1),
            (course_id, "Which symbol is used to assign a value?", "=", "==", ":", "!=", 1),
            (course_id, "Which data type stores True or False?", "String", "Boolean", "Float", "Tuple", 2),
            (course_id, "Which function displays output in Python?", "show()", "echo()", "print()", "display()", 3),
            (course_id, "What does a function help you do?", "Repeat reusable code", "Delete variables", "Install Python", "Open browser", 1),
            (course_id, "OOP in Python is based on?", "Objects and classes", "HTML pages", "Database tables", "Networks", 1),
        ]

    elif course_name == "Machine Learning":
        return [
            (course_id, "What is supervised learning?", "Labeled Data", "Unlabeled Data", "Robotics", "Manual Coding", 1),
            (course_id, "Which algorithm is for classification?", "KNN", "K-Means", "Apriori", "PCA", 1),
            (course_id, "What is overfitting?", "Poor test performance", "Good test performance", "Fast training", "No training", 1),
            (course_id, "Which metric for regression?", "Accuracy", "MSE", "Recall", "Precision", 2),
            (course_id, "Popular ML library?", "NumPy", "Scikit-learn", "Tkinter", "Pygame", 2),
            (course_id, "Training data is used to?", "Teach the model", "Delete errors", "Draw charts", "Host websites", 1),
            (course_id, "K-Means is mainly used for?", "Clustering", "Sorting files", "Encryption", "Web styling", 1),
            (course_id, "Regression models usually predict?", "Continuous values", "Passwords", "Images only", "HTML tags", 1),
            (course_id, "A model with high overfitting performs poorly on?", "New unseen data", "Training data", "Stored files", "CPU", 1),
            (course_id, "Which step comes after training a model?", "Evaluation", "Cooking", "Gaming", "Printing", 1),
        ]

    elif course_name == "Web Development":
        return [
            (course_id, "HTML stands for?", "HyperText Markup Language", "HighText Machine Language", "Hyper Transfer Mark", "None", 1),
            (course_id, "CSS is used for?", "Styling", "Database", "Server", "Security", 1),
            (course_id, "JavaScript runs on?", "Browser", "Database", "OS", "Router", 1),
            (course_id, "Flask is?", "Python Framework", "JS Library", "Database", "Server", 1),
            (course_id, "HTTP stands for?", "HyperText Transfer Protocol", "High Transfer Text", "Hyper Tool Protocol", "None", 1),
            (course_id, "Which tag creates a paragraph?", "<p>", "<div>", "<h1>", "<a>", 1),
            (course_id, "CSS can change a page's?", "Layout and colors", "Electricity", "Compiler", "IP address", 1),
            (course_id, "JavaScript adds?", "Interactivity", "Database tables", "Antivirus", "Cloud storage", 1),
            (course_id, "A responsive website should work on?", "Desktop and mobile", "Desktop only", "Router only", "Printer only", 1),
            (course_id, "Flask is commonly used to build?", "Web apps", "Phone hardware", "Graphics cards", "Operating systems", 1),
        ]

    elif course_name == "Data Science":
        return [
            (course_id, "Data Science involves?", "Data Analysis", "Gaming", "Networking", "Hardware", 1),
            (course_id, "Library for visualization?", "Matplotlib", "Tkinter", "Flask", "Django", 1),
            (course_id, "Pandas is used for?", "Data Handling", "Graphics", "Security", "Deployment", 1),
            (course_id, "EDA stands for?", "Exploratory Data Analysis", "External Data App", "Extra Data Access", "None", 1),
            (course_id, "CSV stands for?", "Comma Separated Values", "Common Secure Value", "Central Save Value", "None", 1),
            (course_id, "Cleaning data means?", "Fixing missing or messy values", "Building hardware", "Drawing cartoons", "Formatting OS", 1),
            (course_id, "A DataFrame is provided by?", "Pandas", "Flask", "HTML", "Linux", 1),
            (course_id, "Charts help with?", "Understanding patterns", "Installing apps", "Encrypting passwords", "Turning off devices", 1),
            (course_id, "EDA is usually done before?", "Model building", "Cooking", "Gaming", "Cloud billing", 1),
            (course_id, "A CSV file mostly stores?", "Tabular data", "Only images", "Videos", "Passwords", 1),
        ]

    elif course_name == "Artificial Intelligence":
        return [
            (course_id, "AI stands for?", "Artificial Intelligence", "Automated Interface", "Advanced Input", "None", 1),
            (course_id, "AI includes?", "ML", "Cooking", "Painting", "Typing", 1),
            (course_id, "Turing Test is for?", "Machine Intelligence", "Security", "Networking", "Database", 1),
            (course_id, "Chatbots use?", "NLP", "CSS", "HTML", "SQL", 1),
            (course_id, "AI field started in?", "1956", "2000", "1995", "1980", 1),
            (course_id, "NLP is mainly about?", "Understanding human language", "Building routers", "Styling pages", "Database indexing", 1),
            (course_id, "A chatbot is an example of?", "AI application", "Computer virus", "Web browser", "Spreadsheet", 1),
            (course_id, "Machine learning is a part of?", "Artificial Intelligence", "Photoshop", "Cloud storage", "Cyber attack", 1),
            (course_id, "AI can be used for?", "Recommendation systems", "Only cooking", "Only typing", "Only painting", 1),
            (course_id, "The Turing Test checks whether a machine can?", "Show intelligent behavior", "Compile code", "Charge a battery", "Create hardware", 1),
        ]

    elif course_name == "Deep Learning":
        return [
            (course_id, "Deep Learning uses?", "Neural Networks", "Trees", "Graphs", "Tables", 1),
            (course_id, "Activation function?", "ReLU", "HTTP", "CSS", "Flask", 1),
            (course_id, "CNN used for?", "Images", "Database", "Security", "Cloud", 1),
            (course_id, "RNN used for?", "Sequence Data", "Images", "Networking", "SQL", 1),
            (course_id, "TensorFlow is?", "DL Framework", "Browser", "Database", "Server", 1),
            (course_id, "Neural networks are inspired by the?", "Human brain", "Traffic lights", "Power supply", "Router", 1),
            (course_id, "ReLU is mainly used to?", "Activate neurons", "Delete files", "Encrypt messages", "Create tables", 1),
            (course_id, "CNN is strong at?", "Image tasks", "Spreadsheet formatting", "Router setup", "Audio cables", 1),
            (course_id, "RNN is often used for?", "Sequences and text", "Only images", "Firewall rules", "Video cables", 1),
            (course_id, "TensorFlow helps developers?", "Build deep learning models", "Design posters", "Browse web pages", "Run databases only", 1),
        ]

    elif course_name == "SQL & Databases":
        return [
            (course_id, "SQL stands for?", "Structured Query Language", "Secure Query Link", "Simple Query Logic", "None", 1),
            (course_id, "SELECT is used for?", "Retrieve Data", "Delete Data", "Insert Data", "Update OS", 1),
            (course_id, "Primary Key is?", "Unique Identifier", "Duplicate Value", "Index Only", "None", 1),
            (course_id, "SQLite is?", "Database", "Browser", "OS", "Language", 1),
            (course_id, "JOIN is used for?", "Combine Tables", "Delete Table", "Update Server", "None", 1),
            (course_id, "INSERT command is used to?", "Add new rows", "Remove tables", "Restart OS", "Compile code", 1),
            (course_id, "A table stores data in?", "Rows and columns", "Slides only", "Videos only", "Networks only", 1),
            (course_id, "A primary key should be?", "Unique", "Empty", "Repeated", "Randomly missing", 1),
            (course_id, "JOIN helps when data is split across?", "Multiple tables", "Browsers", "Operating systems", "Images", 1),
            (course_id, "SQLite is useful for?", "Lightweight local databases", "Styling HTML", "Video editing", "Cloud hosting only", 1),
        ]

    elif course_name == "Cyber Security":
        return [
            (course_id, "Cybersecurity protects?", "Systems", "Cooking", "Painting", "Typing", 1),
            (course_id, "Firewall is?", "Security System", "Database", "Browser", "Router", 1),
            (course_id, "Phishing is?", "Attack", "Programming", "Server", "Cloud", 1),
            (course_id, "Encryption protects?", "Data", "Food", "Music", "Games", 1),
            (course_id, "Ethical hacker is?", "Security Tester", "Criminal", "Developer", "Designer", 1),
            (course_id, "A strong password should be?", "Hard to guess", "Only 3 letters", "Your name", "Always 12345", 1),
            (course_id, "Phishing usually tries to steal?", "Sensitive information", "Food recipes", "Screen brightness", "Printer ink", 1),
            (course_id, "Encryption changes data into?", "Protected unreadable form", "A video", "A browser", "A folder", 1),
            (course_id, "A firewall helps block?", "Unauthorized access", "Course videos", "HTML pages", "Audio files", 1),
            (course_id, "Ethical hacking is done to?", "Improve security", "Damage systems", "Delete all files", "Slow networks", 1),
        ]

    elif course_name == "Cloud Computing":
        return [
            (course_id, "Cloud provides?", "Online Services", "Offline Storage", "Hardware Only", "None", 1),
            (course_id, "AWS is?", "Cloud Platform", "Database", "OS", "Language", 1),
            (course_id, "IaaS means?", "Infrastructure as a Service", "Internet as System", "Internal Service", "None", 1),
            (course_id, "SaaS means?", "Software as a Service", "Secure Access", "System Access", "None", 1),
            (course_id, "Azure is?", "Cloud Platform", "Browser", "OS", "Database", 1),
            (course_id, "Cloud services are accessed over the?", "Internet", "Keyboard only", "Printer", "Monitor", 1),
            (course_id, "SaaS examples usually provide?", "Ready-to-use software", "Only hardware chips", "Power cables", "Game consoles", 1),
            (course_id, "IaaS gives users?", "Virtual infrastructure", "Only wallpapers", "Only text files", "Only browsers", 1),
            (course_id, "AWS and Azure are both?", "Cloud platforms", "Operating systems", "Antivirus tools", "Browsers", 1),
            (course_id, "Cloud can help businesses by offering?", "Scalable resources", "Only offline CDs", "Paper notebooks", "No storage", 1),
        ]

    elif course_name == "Java Programming":
        return [
            (course_id, "Java is?", "Programming Language", "Database", "OS", "Browser", 1),
            (course_id, "JVM stands for?", "Java Virtual Machine", "Java Variable Method", "Joint Virtual Mode", "None", 1),
            (course_id, "OOP stands for?", "Object Oriented Programming", "Online Output Program", "Object Output Protocol", "None", 1),
            (course_id, "Which keyword creates object?", "new", "create", "object", "make", 1),
            (course_id, "Java file extension?", ".java", ".py", ".html", ".sql", 1),
            (course_id, "Java code runs on the?", "JVM", "Router", "Browser only", "Database", 1),
            (course_id, "A class in Java is used as a?", "Blueprint for objects", "Firewall", "Spreadsheet", "Web server", 1),
            (course_id, "Objects are created using?", "new keyword", "print statement", "SELECT query", "HTML tag", 1),
            (course_id, "Java supports which major style?", "Object-oriented programming", "Only markup", "Only styling", "Only networking", 1),
            (course_id, "Compiled Java code usually becomes?", "Bytecode", "JPEG", "CSV", "HTML", 1),
        ]

    elif course_name == "C Programming":
        return [
            (course_id, "C is?", "Programming Language", "Database", "Cloud", "Server", 1),
            (course_id, "Main function?", "main()", "start()", "run()", "execute()", 1),
            (course_id, "Header file?", "stdio.h", "python.h", "java.h", "html.h", 1),
            (course_id, "Printf used for?", "Output", "Input", "Delete", "Compile", 1),
            (course_id, "Pointer stores?", "Address", "Value Only", "String", "None", 1),
            (course_id, "scanf is commonly used for?", "Input", "Output", "Encryption", "Networking", 1),
            (course_id, "A pointer stores the?", "Memory address", "Page title", "Database name", "Video length", 1),
            (course_id, "Header files provide?", "Function declarations", "Only images", "Only passwords", "Only colors", 1),
            (course_id, "main() is the program's?", "Entry point", "Error message", "Comment", "Database", 1),
            (course_id, "printf displays?", "Output on screen", "Firewall rules", "Cloud accounts", "Only folders", 1),
        ]

    elif course_name == "Data Structures":
        return [
            (course_id, "Stack follows?", "LIFO", "FIFO", "Random", "Sorted", 1),
            (course_id, "Queue follows?", "FIFO", "LIFO", "Sorted", "Random", 1),
            (course_id, "Binary Tree max children?", "2", "3", "4", "5", 1),
            (course_id, "Linked list stores?", "Nodes", "Arrays", "Tables", "Graphs", 1),
            (course_id, "Searching technique?", "Binary Search", "Cooking", "Painting", "Typing", 1),
            (course_id, "Stack operations usually happen at the?", "Top", "Bottom only", "Middle only", "Random place", 1),
            (course_id, "Queue is useful when order matters like?", "First come first served", "Random drawing", "Painting", "Typing", 1),
            (course_id, "A linked list is made of?", "Connected nodes", "HTML tags", "Cloud servers", "Only numbers", 1),
            (course_id, "Binary search works best on?", "Sorted data", "Unsorted random data", "Photos", "Videos", 1),
            (course_id, "A tree is useful for representing?", "Hierarchical data", "Only colors", "Only passwords", "Only music", 1),
        ]

    elif course_name == "Operating Systems":
        return [
            (course_id, "OS manages?", "Resources", "Food", "Music", "Games", 1),
            (course_id, "Process is?", "Running Program", "File", "Folder", "Device", 1),
            (course_id, "Deadlock occurs when?", "Resources blocked", "System off", "Update done", "None", 1),
            (course_id, "CPU scheduling?", "Process Management", "Cooking", "Painting", "Typing", 1),
            (course_id, "Linux is?", "Operating System", "Database", "Cloud", "Language", 1),
            (course_id, "An operating system helps users by?", "Managing hardware and software", "Only drawing charts", "Only editing videos", "Only browsing", 1),
            (course_id, "CPU scheduling decides?", "Which process runs next", "Screen color", "Mouse speed only", "Browser theme", 1),
            (course_id, "A process is basically?", "A program in execution", "A network cable", "A database table", "A photo", 1),
            (course_id, "Deadlock is a problem of?", "Competing resources", "HTML formatting", "Audio volume", "Mouse color", 1),
            (course_id, "Linux belongs to the category of?", "Operating systems", "Spreadsheets", "Browsers", "Databases", 1),
        ]

    elif course_name == "Computer Networks":
        return [
            (course_id, "IP stands for?", "Internet Protocol", "Internal Process", "Input Port", "None", 1),
            (course_id, "HTTP used for?", "Web Communication", "Cooking", "Music", "Gaming", 1),
            (course_id, "Router connects?", "Networks", "Files", "Programs", "Apps", 1),
            (course_id, "TCP ensures?", "Reliable Communication", "Fast Gaming", "Cooking", "None", 1),
            (course_id, "OSI layers?", "7", "5", "4", "10", 1),
            (course_id, "A router helps move data between?", "Networks", "Only folders", "Only keyboards", "Only screens", 1),
            (course_id, "HTTP is mostly used on the?", "Web", "Printer only", "Music player", "Calculator", 1),
            (course_id, "TCP is valued because it is?", "Reliable", "Only colorful", "Silent", "Offline only", 1),
            (course_id, "IP is used to identify?", "Devices on a network", "Only books", "Only songs", "Only classes", 1),
            (course_id, "OSI model has how many layers?", "7", "2", "3", "12", 1),
        ]

    elif course_name == "DevOps":
        return [
            (course_id, "DevOps combines?", "Development & Operations", "Design & Ops", "Device & OS", "None", 1),
            (course_id, "CI means?", "Continuous Integration", "Cloud Instance", "Code Input", "None", 1),
            (course_id, "CD means?", "Continuous Deployment", "Code Delete", "Cloud Data", "None", 1),
            (course_id, "Docker is?", "Container Tool", "Database", "OS", "Browser", 1),
            (course_id, "Jenkins used for?", "Automation", "Gaming", "Cooking", "Music", 1),
            (course_id, "DevOps aims to improve?", "Speed and collaboration", "Painting skills", "Music quality", "Typing speed only", 1),
            (course_id, "CI helps teams by?", "Integrating code often", "Deleting servers", "Removing all tests", "Turning off internet", 1),
            (course_id, "CD is about?", "Delivering changes faster", "Color design", "Database backup only", "Drawing diagrams", 1),
            (course_id, "Docker packages apps inside?", "Containers", "Spreadsheets", "Routers", "Slides", 1),
            (course_id, "Jenkins is often used to automate?", "Build and deployment pipelines", "Painting", "Cooking", "Typing lessons", 1),
        ]

    else:
        return []
