import { createGlobalStyle, ThemeProvider } from "styled-components";
import Head from "next/head";

const GlobalStyle = createGlobalStyle`
  body {
    overflow-y: auto;
    margin: 0;
    padding: 0;
    font-family: 'News Cycle', sans-serif;
    box-sizing: border-box;
  }
`;

const theme = {
  colors: {
    primary: "#FFFFFF",
    secondary: "#e3e3e3",
    tertiary: "#c2c2c2",
    main: "#e80000",
    second_main: "#850000",
  },
  backgrounds: {
    primary: "#010409",
    secondary: "#06070a",
    tertiary: "#0b0d12",
  },
};

export default function App({ Component, pageProps }) {
  return (
    <>
      <Head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
        <link rel="shortcut icon" href="/images/favicon.ico" />
        <link
          href="https://fonts.googleapis.com/css2?family=News+Cycle&display=swap"
          rel="stylesheet"
        />
        <title>Codavi</title>
      </Head>
      <GlobalStyle />
      <ThemeProvider theme={theme}>
        <Component {...pageProps} />
      </ThemeProvider>
    </>
  );
}
