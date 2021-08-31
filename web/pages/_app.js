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
    secondary: "#6f6f6f",
  },
  backgrounds: {
    primary: "#010409",
    secondary: "#0d1117",
  },
};

export default function App({ Component, pageProps }) {
  return (
    <>
      <Head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
        <link
          href="https://fonts.googleapis.com/css2?family=News+Cycle&display=swap"
          rel="stylesheet"
        />
      </Head>
      <GlobalStyle />
      <ThemeProvider theme={theme}>
        <Component {...pageProps} />
      </ThemeProvider>
    </>
  );
}
