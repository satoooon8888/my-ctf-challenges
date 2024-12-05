import { Application, helpers } from "https://deno.land/x/oak/mod.ts";

const HOST = "0.0.0.0";
const PORT = 8080;

const VALID_TOKEN = Deno.env.get("VALID_TOKEN");
const FLAG = Deno.env.get("FLAG");

const app = new Application();

app.use((ctx) => {
  const params = helpers.getQuery(ctx);
  if (!params.token) return;

  const token = params.token;
  if (token !== VALID_TOKEN) return;
  
  ctx.response.body = `export const FLAG = "${FLAG}";`;
});

app.addEventListener("listen", ({ hostname, port }) => {
  console.log(`Listening on: ${hostname}:${port}`);
});

await app.listen({ hostname: HOST, port: PORT });
