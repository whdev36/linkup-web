attrs = {
    'placeholder': {
        'email': 'Enter your email',
        'first_name': 'Enter your first name',
        'last_name': 'Enter your last name',
        'username': 'Create username',
        'password1': 'Create password',
        'password2': 'Confirm password',
        'bio': 'Add a bio',
    },
    'label': {
        'email': 'Email',
        'first_name': 'First Name',
        'last_name': 'Last Name',
        'username': 'Username',
        'password1': 'Password',
        'password2': 'Confirm Password',
        'bio': 'Bio',
        'profile_picture': 'Profile Picture',
    },
    'help_text': {
        'email': 'Please enter a valid email address.',
        'first_name': 'Your first name as it appears on official documents.',
        'last_name': 'Your last name as it appears on official documents.',
        'username': 'Choose a unique username for your account.',
        'password1': 'Your password must be at least 8 characters long.',
        'password2': 'Enter the same password as above for verification.',
        'bio': 'Provide a short description about yourself (max 300 characters).',
        'profile_picture': 'Upload a square image (e.g., 300x300 pixels) for best results.',
    },
    'error_messages': {
        'email': {
            'required': 'Email is required.',
            'invalid': 'Enter a valid email address.',
        },
        'username': {
            'required': 'Username is required.',
            'unique': 'This username is already taken.',
        },
        'password1': {
            'required': 'Password is required.',
            'too_short': 'Password must be at least 8 characters.',
        },
        'password2': {
            'required': 'Please confirm your password.',
            'mismatch': 'Passwords do not match.',
        },
        'bio': {
            'max_length': 'Bio cannot exceed 300 characters.',
        },
        'profile_picture': {
            'invalid': 'Please upload a valid image file.',
            'max_length': 'The file name is too long.',
        },
    }
}