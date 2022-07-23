import psycopg2

class database():
	def __init__(self) -> None:
		self.conn = None
		self.database = "d4dv34dbvjjebc"
		self.user 	  = "xfbufavhetsiza" 
		self.password = "b6d5807952f7033be5f26b4fb48f0166fe1b2a888f443634c3cf322971534814"
		self.host     = "ec2-54-87-179-4.compute-1.amazonaws.com"
		self.port	  = "5432"

	def connect(self):
		self.conn = psycopg2.connect(database = self.database,
									user 	  = self.user,
									password  = self.password,
									host	  = self.host,
									port	  = self.port)
		print("connect database successfully")
		self.cursor = self.conn.cursor()

	def create_table(self):
		self.cursor.execute("CREATE TABLE userdata (id serial PRIMARY KEY, name VARCHAR(50), userid VARCHAR(50));")

	def update_table(self):
		self.cursor.execute("UPDATE userdata SET name = %s WHERE userid = %s;", ("test", "banana"))

	def close(self):
		# Clean up
		self.conn.commit()
		self.conn.close()
		self.conn.close()