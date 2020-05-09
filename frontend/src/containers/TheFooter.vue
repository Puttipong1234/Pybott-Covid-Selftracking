<template>
  <CFooter :fixed="false">
    <div>
      <a href="https://www.facebook.com/Pybott/" target="_blank">PYBOTT</a>
      <span class="ml-1">&copy; {{new Date().getFullYear()}}</span>
    </div>
    <div class="ml-auto">
      <span class="mr-1">Powered by</span>
      <a href="https://www.facebook.com/Pybott/" target="_blank">PYBOTT THAILAND</a>
    </div>
  </CFooter>
</template>

<script>
export default {
  name: 'TheFooter'
}
</script>
