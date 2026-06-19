def with_parts(lesson_items):
    lessons_with_parts = []
    for index, lesson in enumerate(lesson_items, start=1):
        lesson_copy = dict(lesson)
        if not lesson_copy["title"].startswith("Part "):
            lesson_copy["title"] = f"Part {index}: {lesson_copy['title']}"
        lessons_with_parts.append(lesson_copy)
    return lessons_with_parts


SUPPLEMENTAL_LESSON_VIDEOS = {
    "Python Programming": "https://www.youtube.com/embed/kqtD5dpn9C8",
    "Machine Learning": "https://www.youtube.com/embed/GwIo3gDZCVQ",
    "Web Development": "https://www.youtube.com/embed/W6NZfCO5SIk",
    "Data Science": "https://www.youtube.com/embed/X3paOmcrTjQ",
    "Artificial Intelligence": "https://www.youtube.com/embed/JMUxmLyrhSk",
    "Deep Learning": "https://www.youtube.com/embed/aircAruvnKk",
    "SQL & Databases": "https://www.youtube.com/embed/HXV3zeQKqGY",
    "Cyber Security": "https://www.youtube.com/embed/inWWhr5tnEA",
    "Cloud Computing": "https://www.youtube.com/embed/M988_fsOSWo",
    "Java Programming": "https://www.youtube.com/embed/eIrMbAQSU34",
    "C Programming": "https://www.youtube.com/embed/KJgsSFOSQv0",
    "Data Structures": "https://www.youtube.com/embed/RBSGKlAvoiM",
    "Operating Systems": "https://www.youtube.com/embed/26QPDBe-NB8",
    "Computer Networks": "https://www.youtube.com/embed/qiQR5rTSshw",
    "DevOps": "https://www.youtube.com/embed/0yWAtQ6wYNM",
}


def ensure_minimum_lessons(course_name, level, lesson_items, minimum=3):
    lessons = list(lesson_items)
    while len(lessons) < minimum:
        lessons.append({
            "title": f"{course_name} {level} Practice Review",
            "video": SUPPLEMENTAL_LESSON_VIDEOS.get(course_name, "https://www.youtube.com/embed/rfscVS0vtbw"),
            "test": False,
        })
    return lessons


def get_course_lessons(course_name, level="Beginner"):
    normalized_level = (level or "Beginner").title()
    if normalized_level not in {"Beginner", "Intermediate", "Advanced"}:
        normalized_level = "Beginner"

    lessons = {
        "Python Programming": {
            "Beginner": [
                {"title": "Python Introduction", "video": "https://www.youtube.com/embed/rfscVS0vtbw", "test": False},
                {"title": "Python Variables", "video": "https://www.youtube.com/embed/kqtD5dpn9C8", "test": True},
                {"title": "Python Functions", "video": "https://www.youtube.com/embed/9Os0o3wzS_I", "test": False},
                {"title": "Python OOP", "video": "https://www.youtube.com/embed/JeznW_7DlB0", "test": True},
            ],
            "Intermediate": [
                {"title": "Python Crash Course", "video": "https://www.youtube.com/embed/_uQrJ0TkZlc", "test": False},
                {"title": "Python Data Structures", "video": "https://www.youtube.com/embed/W8KRzm-HUcc", "test": True},
                {"title": "Functions and Modules", "video": "https://www.youtube.com/embed/CqvZ3vGoGs0", "test": False},
                {"title": "OOP Practice", "video": "https://www.youtube.com/embed/apACNr7DC_s", "test": True},
            ],
            "Advanced": [
                {"title": "Advanced Python Concepts", "video": "https://www.youtube.com/embed/HGOBQPFzWKo", "test": False},
                {"title": "Decorators and Generators", "video": "https://www.youtube.com/embed/FsAPt_9Bf3U", "test": True},
                {"title": "Object-Oriented Design", "video": "https://www.youtube.com/embed/Ej_02ICOIgs", "test": False},
                {"title": "Production Python Tips", "video": "https://www.youtube.com/embed/OA3D2mB16k8", "test": True},
            ],
        },
        "Machine Learning": {
            "Beginner": [
                {"title": "ML Introduction", "video": "https://www.youtube.com/embed/GwIo3gDZCVQ", "test": False},
                {"title": "Supervised Learning", "video": "https://www.youtube.com/embed/ukzFI9rgwfU", "test": True},
                {"title": "Regression Models", "video": "https://www.youtube.com/embed/PaFPbb66DxQ", "test": False},
            ],
            "Intermediate": [
                {"title": "Machine Learning Roadmap", "video": "https://www.youtube.com/embed/i_LwzRVP7bg", "test": False},
                {"title": "Classification Basics", "video": "https://www.youtube.com/embed/0Lt9w-BxKFQ", "test": True},
                {"title": "Model Evaluation", "video": "https://www.youtube.com/embed/p_jJXJ_u2pk", "test": False},
            ],
            "Advanced": [
                {"title": "Bias Variance Tradeoff", "video": "https://www.youtube.com/embed/EuBBz3bI-aA", "test": False},
                {"title": "Advanced Model Tuning", "video": "https://www.youtube.com/embed/6dbrR-WymjI", "test": True},
                {"title": "Cross Validation and Metrics", "video": "https://www.youtube.com/embed/fSytzGwwBVw", "test": False},
            ],
        },
        "Web Development": {
            "Beginner": [
                {"title": "HTML Basics", "video": "https://www.youtube.com/embed/pQN-pnXPaVg", "test": False},
                {"title": "CSS Styling", "video": "https://www.youtube.com/embed/1Rs2ND1ryYc", "test": True},
                {"title": "JavaScript Basics", "video": "https://www.youtube.com/embed/W6NZfCO5SIk", "test": False},
            ],
            "Intermediate": [
                {"title": "Responsive Web Design", "video": "https://www.youtube.com/embed/srvUrASNj0s", "test": False},
                {"title": "Modern CSS Layout", "video": "https://www.youtube.com/embed/jV8B24rSN5o", "test": True},
                {"title": "Interactive JavaScript", "video": "https://www.youtube.com/embed/jS4aFq5-91M", "test": False},
            ],
            "Advanced": [
                {"title": "Frontend Architecture", "video": "https://www.youtube.com/embed/4UZrsTqkcW4", "test": False},
                {"title": "Advanced JavaScript Concepts", "video": "https://www.youtube.com/embed/9emXNzqCKyg", "test": True},
                {"title": "Performance and Optimization", "video": "https://www.youtube.com/embed/0fONene3OIA", "test": False},
            ],
        },
        "Data Science": {
            "Beginner": [
                {"title": "Data Science Intro", "video": "https://www.youtube.com/embed/X3paOmcrTjQ", "test": False},
                {"title": "Data Analysis", "video": "https://www.youtube.com/embed/r-uOLxNrNk8", "test": True},
            ],
            "Intermediate": [
                {"title": "Pandas Fundamentals", "video": "https://www.youtube.com/embed/vmEHCJofslg", "test": False},
                {"title": "Data Cleaning Workflow", "video": "https://www.youtube.com/embed/bDhvCp3_lYw", "test": True},
            ],
            "Advanced": [
                {"title": "Exploratory Data Analysis", "video": "https://www.youtube.com/embed/-o3AxdVcUtQ", "test": False},
                {"title": "Feature Engineering Basics", "video": "https://www.youtube.com/embed/N9fDIAflCMY", "test": True},
            ],
        },
        "Artificial Intelligence": {
            "Beginner": [
                {"title": "AI Introduction", "video": "https://www.youtube.com/embed/JMUxmLyrhSk", "test": False},
                {"title": "AI Applications", "video": "https://www.youtube.com/embed/2ePf9rue1Ao", "test": True},
            ],
            "Intermediate": [
                {"title": "AI Concepts Overview", "video": "https://www.youtube.com/embed/ad79nYk2keg", "test": False},
                {"title": "NLP and Chatbots", "video": "https://www.youtube.com/embed/fOvTtapxa9c", "test": True},
            ],
            "Advanced": [
                {"title": "Intelligent Systems Design", "video": "https://www.youtube.com/embed/gpP_YEv_9jA", "test": False},
                {"title": "AI Ethics and Applications", "video": "https://www.youtube.com/embed/HoKRLlLKMw8", "test": True},
            ],
        },
        "Deep Learning": {
            "Beginner": [
                {"title": "Neural Networks", "video": "https://www.youtube.com/embed/aircAruvnKk", "test": False},
                {"title": "Deep Learning Basics", "video": "https://www.youtube.com/embed/6M5VXKLf4D4", "test": True},
            ],
            "Intermediate": [
                {"title": "Neural Network Training", "video": "https://www.youtube.com/embed/IHZwWFHWa-w", "test": False},
                {"title": "CNN and Vision Basics", "video": "https://www.youtube.com/embed/YRhxdVk_sIs", "test": True},
            ],
            "Advanced": [
                {"title": "Advanced Deep Learning", "video": "https://www.youtube.com/embed/tPYj3fFJGjk", "test": False},
                {"title": "Sequence Models and RNNs", "video": "https://www.youtube.com/embed/UNmqTiOnRfg", "test": True},
            ],
        },
        "SQL & Databases": {
            "Beginner": [
                {"title": "SQL Basics", "video": "https://www.youtube.com/embed/HXV3zeQKqGY", "test": False},
                {"title": "SQL Joins", "video": "https://www.youtube.com/embed/9yeOJ0ZMUYw", "test": True},
            ],
            "Intermediate": [
                {"title": "Database Design Basics", "video": "https://www.youtube.com/embed/ztHopE5Wnpc", "test": False},
                {"title": "Intermediate SQL Queries", "video": "https://www.youtube.com/embed/7S_tz1z_5bA", "test": True},
            ],
            "Advanced": [
                {"title": "SQL Optimization", "video": "https://www.youtube.com/embed/HubezKbFL7E", "test": False},
                {"title": "Indexing and Performance", "video": "https://www.youtube.com/embed/v5S8UO4vW7Q", "test": True},
            ],
        },
        "Cyber Security": {
            "Beginner": [
                {"title": "Cyber Security Basics", "video": "https://www.youtube.com/embed/inWWhr5tnEA", "test": False},
                {"title": "Ethical Hacking Intro", "video": "https://www.youtube.com/embed/3Kq1MIfTWCE", "test": True},
            ],
            "Intermediate": [
                {"title": "Security Fundamentals", "video": "https://www.youtube.com/embed/U_P23SqJaDc", "test": False},
                {"title": "Common Attack Types", "video": "https://www.youtube.com/embed/shQEXpUwaIY", "test": True},
            ],
            "Advanced": [
                {"title": "Network Security Concepts", "video": "https://www.youtube.com/embed/yo7J11Ti6uw", "test": False},
                {"title": "Advanced Ethical Hacking", "video": "https://www.youtube.com/embed/FXl3i2nR1B0", "test": True},
            ],
        },
        "Cloud Computing": {
            "Beginner": [
                {"title": "Cloud Basics", "video": "https://www.youtube.com/embed/M988_fsOSWo", "test": False},
                {"title": "AWS Introduction", "video": "https://www.youtube.com/embed/ulprqHHWlng", "test": True},
            ],
            "Intermediate": [
                {"title": "Cloud Service Models", "video": "https://www.youtube.com/embed/2LaAJq1lB1Q", "test": False},
                {"title": "AWS Core Services", "video": "https://www.youtube.com/embed/IA90BTozdow", "test": True},
            ],
            "Advanced": [
                {"title": "Cloud Architecture", "video": "https://www.youtube.com/embed/k1RI5locZE4", "test": False},
                {"title": "Scalability and Deployment", "video": "https://www.youtube.com/embed/3hLmDS179YE", "test": True},
            ],
        },
        "Java Programming": {
            "Beginner": [
                {"title": "Java Basics", "video": "https://www.youtube.com/embed/eIrMbAQSU34", "test": False},
                {"title": "Java OOP", "video": "https://www.youtube.com/embed/UmnCZ7-9yDY", "test": True},
            ],
            "Intermediate": [
                {"title": "Java Classes and Objects", "video": "https://www.youtube.com/embed/w0xT64L7sT4", "test": False},
                {"title": "Intermediate Java OOP", "video": "https://www.youtube.com/embed/xk4_1vDrzzo", "test": True},
            ],
            "Advanced": [
                {"title": "Advanced Java Concepts", "video": "https://www.youtube.com/embed/grEKMHGYyns", "test": False},
                {"title": "Collections and Design", "video": "https://www.youtube.com/embed/VE_AAUxTUCY", "test": True},
            ],
        },
        "C Programming": {
            "Beginner": [
                {"title": "C Introduction", "video": "https://www.youtube.com/embed/KJgsSFOSQv0", "test": False},
                {"title": "C Functions", "video": "https://www.youtube.com/embed/ZSPZob_1TOk", "test": True},
            ],
            "Intermediate": [
                {"title": "Pointers and Arrays", "video": "https://www.youtube.com/embed/zuegQmMdy8M", "test": False},
                {"title": "Functions and Memory", "video": "https://www.youtube.com/embed/NLXJQTs7ZsM", "test": True},
            ],
            "Advanced": [
                {"title": "Advanced C Programming", "video": "https://www.youtube.com/embed/Bz4MxDeEM6k", "test": False},
                {"title": "Pointers Deep Dive", "video": "https://www.youtube.com/embed/q24-QTbKQS8", "test": True},
            ],
        },
        "Data Structures": {
            "Beginner": [
                {"title": "DSA Basics", "video": "https://www.youtube.com/embed/RBSGKlAvoiM", "test": False},
                {"title": "Linked List", "video": "https://www.youtube.com/embed/Nq7ok-OyEpg", "test": True},
            ],
            "Intermediate": [
                {"title": "Stacks and Queues", "video": "https://www.youtube.com/embed/wjI1WNcIntg", "test": False},
                {"title": "Trees and Traversal", "video": "https://www.youtube.com/embed/oSWTXtMglKE", "test": True},
            ],
            "Advanced": [
                {"title": "Advanced DSA Strategy", "video": "https://www.youtube.com/embed/8hly31xKli0", "test": False},
                {"title": "Binary Search and Complexity", "video": "https://www.youtube.com/embed/MHf6awe89xw", "test": True},
            ],
        },
        "Operating Systems": {
            "Beginner": [
                {"title": "OS Introduction", "video": "https://www.youtube.com/embed/26QPDBe-NB8", "test": False},
                {"title": "Process Management", "video": "https://www.youtube.com/embed/vBURTt97EkA", "test": True},
            ],
            "Intermediate": [
                {"title": "Threads and Scheduling", "video": "https://www.youtube.com/embed/4ni-22eynOY", "test": False},
                {"title": "Memory Management", "video": "https://www.youtube.com/embed/F-x5sY2dR8M", "test": True},
            ],
            "Advanced": [
                {"title": "Deadlocks and Synchronization", "video": "https://www.youtube.com/embed/pqp96lDklD4", "test": False},
                {"title": "Advanced OS Topics", "video": "https://www.youtube.com/embed/dv4mXBsv6TI", "test": True},
            ],
        },
        "Computer Networks": {
            "Beginner": [
                {"title": "Networking Basics", "video": "https://www.youtube.com/embed/qiQR5rTSshw", "test": False},
                {"title": "OSI Model", "video": "https://www.youtube.com/embed/vv4y_uOneC0", "test": True},
            ],
            "Intermediate": [
                {"title": "TCP IP Explained", "video": "https://www.youtube.com/embed/keeqnciDVOo", "test": False},
                {"title": "Routing and Switching", "video": "https://www.youtube.com/embed/1z0ULvg_pW8", "test": True},
            ],
            "Advanced": [
                {"title": "Advanced Networking Concepts", "video": "https://www.youtube.com/embed/cNwEVYkx2Kk", "test": False},
                {"title": "Transport and Reliability", "video": "https://www.youtube.com/embed/LXbDg1v65Qs", "test": True},
            ],
        },
        "DevOps": {
            "Beginner": [
                {"title": "DevOps Introduction", "video": "https://www.youtube.com/embed/0yWAtQ6wYNM", "test": False},
                {"title": "CI/CD Pipeline", "video": "https://www.youtube.com/embed/scEDHsr3APg", "test": True},
            ],
            "Intermediate": [
                {"title": "Docker and Containers", "video": "https://www.youtube.com/embed/3c-iBn73dDE", "test": False},
                {"title": "Jenkins Workflow", "video": "https://www.youtube.com/embed/7KCS70sCoK0", "test": True},
            ],
            "Advanced": [
                {"title": "Advanced DevOps Practices", "video": "https://www.youtube.com/embed/j5Zsa_eOXeY", "test": False},
                {"title": "Infrastructure Automation", "video": "https://www.youtube.com/embed/S8eX0MxfnB4", "test": True},
            ],
        },
    }

    course_levels = lessons.get(course_name, {})
    selected_lessons = course_levels.get(normalized_level, course_levels.get("Beginner", []))
    selected_lessons = ensure_minimum_lessons(course_name, normalized_level, selected_lessons)
    return with_parts(selected_lessons)
