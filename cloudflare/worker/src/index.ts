// Provisioning Worker skeleton. See docs/adr/0006-provisioning-worker.md.
// No logic yet: every request returns 501.

export interface Env {
  CF_API_TOKEN: string;
}

export default {
  async fetch(_request: Request, _env: Env): Promise<Response> {
    return Response.json({ error: "not_implemented" }, { status: 501 });
  },
} satisfies ExportedHandler<Env>;
