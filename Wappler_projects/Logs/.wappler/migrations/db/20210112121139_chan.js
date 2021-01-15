
exports.up = function(knex) {
  return knex.schema
    .table('userinfo', function (table) {
      table.string('loginuser_id');
    })
    .table('users', function (table) {
      table.string('regitster_id');
    })
};

exports.down = function(knex) {
  return knex.schema
    .table('userinfo', function (table) {
      table.dropColumn('loginuser_id');
    })
    .table('users', function (table) {
      table.dropColumn('regitster_id');
    })
};
