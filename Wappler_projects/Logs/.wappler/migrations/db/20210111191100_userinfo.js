
exports.up = function(knex) {
  return knex.schema
    .createTable('userinfo', function (table) {
      table.increments('id');
      table.string('username');
      table.string('password');
    })
    .then(() => {return knex('userinfo').insert({"username":"suhail767@gmail.com","id":"1","password":"qwerty231"})
})};

exports.down = function(knex) {
  return knex.schema
    .dropTable('userinfo')
};
