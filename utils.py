import os


def getBaseDir():
    base_dir = input('Output directory: ')
    if not os.path.exists(base_dir):
        os.mkdir(base_dir)
    return base_dir

def getCourseDir(base_dir, username, course_name):
    user_dir = os.path.join(base_dir, username)
    if not os.path.exists(user_dir):
        os.mkdir(user_dir)
    course_dir = os.path.join(user_dir, course_name)
    if not os.path.exists(course_name):
    	os.mkdir(course_dir)
    return course_dir
    