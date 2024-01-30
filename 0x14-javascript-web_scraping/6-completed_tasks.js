#!/usr/bin/node

const requestModule = require('request');
const apiUrl = process.argv[2];
const completedTasksByUser = {};

function countCompletedTasks(todo) {
  if (todo.completed) {
    const userId = todo.userId.toString();
    completedTasksByUser[userId] = completedTasksByUser[userId] + 1 || 1;
  }
}

requestModule(apiUrl, (error, response, body) => {
  if (error) throw error;
  if (response.statusCode === 200) {
    JSON.parse(body).forEach(countCompletedTasks);
    console.log(completedTasksByUser);
  }
});
