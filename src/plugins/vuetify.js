/**
 * plugins/vuetify.js
 *
 * Framework documentation: https://vuetifyjs.com`
 */

// Styles
import "vuetify/styles";
import { createVuetify } from "vuetify";
import { aliases, mdi } from "vuetify/iconsets/mdi-svg";

import {
  mdiDownloadBoxOutline,
  mdiHeart,
  mdiDownload,
  mdiMicrosoftWindows,
  mdiApple,
  mdiServer,
  mdiGithub,
  mdiWeb,
} from "@mdi/js";

// Composables

// https://vuetifyjs.com/en/introduction/why-vuetify/#feature-guides
export default createVuetify({
  theme: {
    defaultTheme: "dark",
  },
  icons: {
    defaultSet: "mdi",
    aliases: {
      aliases,
      downloadbox: mdiDownloadBoxOutline,
      heart: mdiHeart,
      download: mdiDownload,
      windows: mdiMicrosoftWindows,
      macos: mdiApple,
      server: mdiServer,
      github: mdiGithub,
      web: mdiWeb,
    },
    
    sets: {
      mdi,
    },
  },
});
