import Vue from 'vue';
import Router from 'vue-router';
import todoList from '../components/todoList.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Todo List',
      component: todoList,
    },
  ],
});
