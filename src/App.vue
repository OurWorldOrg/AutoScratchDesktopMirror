<template>
  <v-app>
    <v-main>
      <v-toolbar elevation="4">
        <v-app-bar-nav-icon>
          <v-icon>mdi-download-box-outline</v-icon>
        </v-app-bar-nav-icon>
        <v-toolbar-title>Auto Scratch-Desktop Mirror</v-toolbar-title>
      </v-toolbar>
      <v-container class="d-flex mt-5">
        <v-row class="mx-5">
          <v-col>
            <div class="text-body-1">
              Auto Scratch-Desktop Mirror 是一个基于 GitHub Action 的开源镜像项目，它会每周自动从 Scratch 官方网站下载最新的 Scratch 3.0 安装包并上传至
              GitHub Release 提供给用户以供下载。
              <p class="font-weight-light mt-2 text-caption">
                项目开源于 <a href="https://github.com/sunwuyuan/AutoScratchDesktopMirror">GitHub</a>，此站点由 <a
                  href="https://wuyuan.dev">孙悟元</a>(<a href="https://zerocat.wuyuan.dev">ZeroCat社区</a>) 维护。
                <br />
                感谢: Scratch Team, GitHub, Vue.js, Vuetify.js 以及所有为这个项目添砖加瓦的人们!
                <br />
              </p>
            </div>
          </v-col>
          <v-col>
            <v-card elevation="2">
              <v-card-title>下载 Scratch 3.0</v-card-title>
              <v-card-text>
                未正确加载下载地址？您可以尝试在 <a href="https://zerocat.wuyuan.dev">ZeroCat</a> 在线编程
                ，或在应用商店中下载 <a href="https://apps.apple.com/cn/app/scratch-desktop/id1446785996?mt=12">Mac OS 版本</a> 和 <a
                  href="https://www.microsoft.com/zh-cn/p/scratch-3/9pfgj25jl6x3">Windows 10 以上版本</a> 的 Scratch 桌面版。
                <br />
                <p class="mt-2 font-weight-bold">
                  该版本镜像于 {{ release.date }}，Scratch 版本为 {{ release.scratch_version }}。
                </p>

              </v-card-text>
              <v-card-actions>
                <v-btn color="primary" v-bind:disabled="release.stat == 0"
                  v-bind:href="`https://${download_source.abbr}${release.url.windows}`" text>
                  <v-icon right>mdi-microsoft-windows</v-icon>
                  Windows 下载
                </v-btn>
                <v-btn color="primary" v-bind:disabled="release.stat == 0"
                  v-bind:href="`https://${download_source.abbr}${release.url.macos}`" text>
                  <v-icon right>mdi-apple</v-icon>
                  MacOS 下载
                </v-btn></v-card-actions>
            </v-card>
            <v-card elevation="2" class="mt-7">
              <v-card-title>设置下载源</v-card-title>
              <v-card-text>
                本站默认使用<b> ghproxy 镜像源</b><br />
                通常情况下您<b>不需要更改下载源</b>，但如果默认下载源不可用，您可以更改为另外一个，或者自定义下载源。
                <br /> <br />
                <v-select v-model="download_source" :hint="`${download_source.state}, ${download_source.abbr}`"
                  :items="download_source_items" item-title="state" item-value="abbr" label="Select" persistent-hint
                  return-object single-line></v-select><br /><v-text-field label="可直接编辑"
                  v-model="download_source.abbr"></v-text-field>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-container>

    </v-main>
    <AppFooter />
  </v-app>
</template>

<script>
import axios from 'axios'

import AppFooter from './components/AppFooter.vue';
export default {
  data() {
    return {
      release: {
        stat: 0, // 0 => 加载中，1 => 加载成功，其他 => 加载失败:错误信息
        url: {
          windows: '',
          macos: ''
        },
        date: '一周以内',
        scratch_version: '未知'
      },
      download_source: { state: 'ghproxy', abbr: 'mirror.ghproxy.com/https://github.com' },

      download_source_items: [
        { state: 'Github', abbr: 'github.com' },
        { state: 'gh.api.99988866.xyz', abbr: 'gh.api.99988866.xyz/https://github.com' },
        { state: 'ghproxy', abbr: 'mirror.ghproxy.com/https://github.com' },
        { state: '自定义', abbr: 'github.com' },

      ],

    };

  },

  created() {
    this.release.stat = 0
    axios.get('https://zerocat-static.wuyuan.dev/repos/sunwuyuan/AutoScratchDesktopMirror/releases/latest')
      .then(res => {
        this.release.stat = 1
        this.release.url.windows = res.data.assets.
          filter((element) => { return (element['name'] == "scratch-win.exe") })[0]
          .browser_download_url
          .replace('https://github.com', '')
        this.release.url.macos = res.data.assets.
          filter((element) => { return (element['name'] == "scratch-mac.dmg") })[0]
          .browser_download_url
          .replace('https://github.com', '')
        this.release.date = new Date(res.data.published_at).toLocaleString()
        this.release.scratch_version = JSON.parse(res.data.body).scratch_version
      })
      .catch(err => {
        this.release.stat = err.response.status
      })
  },
};

</script>
