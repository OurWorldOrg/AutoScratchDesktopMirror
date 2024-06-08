<template>
  <v-footer height="40" app>
    <a v-for="item in items" :key="item.title" :href="item.href" :title="item.title"
      class="d-inline-block mx-2 social-link" rel="noopener noreferrer" target="_blank">
      <v-icon :icon="item.icon" :size="item.icon === '$web' ? 24 : 16" />
    </a>

    <div class="text-caption text-disabled" style="position: absolute; right: 16px;">
      {{ (new Date()) }} <a class="text-decoration-none on-surface" href="https://wuyuan.dev/"
        rel="noopener noreferrer" target="_blank">孙悟元</a>
      —
      <a class="text-decoration-none on-surface" href="https://zerocat.wuyuan.dev/" rel="noopener noreferrer"
        target="_blank">
        ZeroCat社区
      </a>
    </div>
  </v-footer>
</template>

<script setup>
const items = [
{
    title: 'ZeroCat社区',
    icon: '$web',
    href: 'https://zerocat.wuyuan.dev/',
  },
  {
    title: 'Github',
    icon: `$github`,
    href: 'https://github.com/zerocatdev/zerocat',
  }
  
]
</script>

<style scoped lang="sass">
  .social-link :deep(.v-icon)
    color: rgba(var(--v-theme-on-background), var(--v-disabled-opacity))
    text-decoration: none
    transition: .2s ease-in-out

    &:hover
      color: rgba(25, 118, 210, 1)
</style>
