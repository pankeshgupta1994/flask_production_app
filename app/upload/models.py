import os
from werkzeug.utils import secure_filename
from app.__init__ import ALLOWED_EXTENSIONS,UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def uploaded_files(file):
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(UPLOAD_FOLDER,filename))
		file_path = UPLOAD_FOLDER + "/" +str(filename)
		return file_path