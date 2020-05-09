import Vue from 'vue'
import Router from 'vue-router'

// Containers
const TheContainer = () => import('@/containers/TheContainer')
const Dashboard = () => import('@/views/dashboard')
const DashboardDev = () => import('@/views/dashboard dev')
const Polls = () => import('@/views/Polls')

Vue.use(Router)

export default new Router({
  mode: 'history', // https://router.vuejs.org/api/#mode
  linkActiveClass: 'active',
  scrollBehavior: () => ({ y: 0 }),
  routes: configRoutes()
})

function configRoutes () {
  return [
    {
      path: '/',
      redirect: '/dashboard',
      name: 'Home',
      component: TheContainer,
      children: [
        {
          path: '/dashboard',
          name: 'Dashboard',
          component: Dashboard
        },
        {
          path: '/DashboardDev',
          name: 'DashboardDev',
          component: DashboardDev
        },
        {
          path: '/polls',
          name: 'polls',
          component: Polls
        },
      ]
    },
  ]
}

