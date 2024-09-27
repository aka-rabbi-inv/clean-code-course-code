let sqlDriver: any;
let mongoDbDriver: any;

// Acts as an adapter, connecting models to various database engines (SQL, MongoDB)
class Database {
  private dbEngine: any;

  loadDatabaseDriver(driver: string) {
    if (driver === 'sql') {
      this.dbEngine = sqlDriver;
    } else {
      this.dbEngine = mongoDbDriver;
    }
  }

  connect() {
    this.dbEngine.connect();
  }

  insertData(data: any) {
    this.dbEngine.insert(data); // updates a user, even though method name is insert
  }

  findOne(id: string) {
    // Todo: Needs to be implemented
  }
}
