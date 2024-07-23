### Shared Exercise Platform

#### 1. Introduction
Design a platform where students can upload and share questions. Students should be able to test themselves on it.

#### 2. Basic Requirements
- **GUI Libraries**: Use libraries such as Tkinter, PyQt5, or other Python-supported front-end and back-end frameworks.
- **Question Formats**: Include various formats such as multiple choice and fill in the blanks. Obtain questions on your own.
- **Interface**: Should be aesthetically pleasing but not overly fancy to distract from problem-solving. Additional features should be user-friendly and easy to use.

#### 3. Required Assignment
- **Basic Requirements**:
  - User and administrator registration, login, and personal information management.
- **User Groups**:
  - Users can choose to create and join groups.
  - Users can search and join groups voluntarily.
- **Upload**:
  - Recognize text in PDF or pictures automatically using OCR.
  - Extracted text results can be edited to complete the input of questions.
- **Question Groups**:
  - Organize questions into categories based on chapters or other criteria.
  - Users can choose a specific group of questions to work on.
  - Design problem-solving interface according to individual preferences.
- **Question Sharing**:
  - Users can share a group of questions with a specific group or make them available to everyone.
  - Recipients of the shared questions gain access to the question group.
- **Search for Groups**:
  - The search should have customizable parameters.
  - Search scope should include shared question groups and the user's uploaded questions, but not question groups that have not been shared.
- **Error Log**:
  - Based on user's incorrect answers and frequency of errors, generate a set of questions that the user should prioritize re-solving using a scientifically effective algorithm.

#### 4. Optional Assignment
- **Sensitive Words Screening**:
  - Implement functionality to screen sensitive words and remove them from the question bank.
- **Visualize Student Abilities**:
  - Define a conversion standard from student's incorrect question information to student's ability information.
  - Create a graph showing the change in student abilities over time.
- **Additional Features**:
  - Implement additional features as desired, earning extra points based on practicality and workload.

---

### Task Framework and Implementation Process

#### Step 1: Setup Environment
- Install Python and required libraries:
  - Tkinter or PyQt5 for GUI
  - OCR library (such as pytesseract)
  - Database (such as SQLite or PostgreSQL)

#### Step 2: User and Admin Management

- **Registration and Login**:
  - Create user and admin registration and login forms.
  - Implement personal information management.
  
#### Step 3: Group Management
- **Creating and Joining Groups**:
  - Allow users to create groups.
  - Implement search functionality for users to find and join groups.

#### Step 4: Upload and OCR Integration
- **File Upload**:
  - Implement file upload functionality for PDF and images.
- **OCR Processing**:
  - Integrate OCR to extract text from uploaded files.
  - Allow users to edit extracted text to complete the input of questions.

#### Step 5: Question Management
- **Organizing Questions**:
  - Design data structures to categorize questions based on chapters or criteria.
  - Implement the problem-solving interface for users.

#### Step 6: Sharing Questions
- **Question Sharing**:
  - Implement functionality to share question groups with specific groups or make them public.
  - Ensure recipients can access shared question groups.

#### Step 7: Search Functionality
- **Customizable Search**:
  - Implement search functionality with customizable parameters.
  - Ensure search includes shared and uploaded question groups only.

#### Step 8: Error Log and Recommendation
- **Error Analysis**:
  - Track user errors and frequency.
- **Recommendation Algorithm**:
  - Implement an algorithm to recommend questions for re-solving based on user errors.

#### Optional Features

#### Step 9: Sensitive Words Screening
- **Sensitive Words Filtering**:
  - Implement functionality to screen and remove sensitive words from the question bank.

#### Step 10: Visualize Student Abilities
- **Ability Conversion**:
  - Define standards to convert incorrect question information to ability metrics.
- **Graph Visualization**:
  - Create graphs showing the change in student abilities over time.

#### Step 11: Additional Features
- **Extra Features**:
  - Implement additional features based on practicality and workload to enhance the platform.

---

This framework provides a structured approach to developing the Shared Exercise Platform. Adjust and expand each step based on the specific requirements and complexity of the features you plan to implement.