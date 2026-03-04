import { Search, BarChart3, Code, Database, ArrowRight } from "lucide-react";
import { Button } from "@/components/ui/button";

function App() {
  const features = [
    {
      icon: <Search className="h-6 w-6" />,
      title: "Search & Connect",
      description:
        "Browse thousands of datasets from data.gouv.fr. Find data on economy, environment, transport, and more.",
    },
    {
      icon: <BarChart3 className="h-6 w-6" />,
      title: "Auto-Generate Dashboards",
      description:
        "Our AI analyzes your data and creates relevant visualizations automatically. Bar charts, line graphs, pie charts, and stats.",
    },
    {
      icon: <Code className="h-6 w-6" />,
      title: "Transparent SQL",
      description:
        "See exactly what queries are run to generate each visualization. Full transparency into how your data is processed.",
    },
  ];

  const steps = [
    { number: "1", title: "Search", description: "Find datasets on data.gouv.fr" },
    { number: "2", title: "Select", description: "Choose a data resource" },
    { number: "3", title: "Analyze", description: "We auto-detect data types" },
    { number: "4", title: "Visualize", description: "Dashboard generates instantly" },
  ];

  return (
    <div className="min-h-screen bg-background">
      {/* Header */}
      <header className="border-b">
        <div className="container mx-auto px-4 h-16 flex items-center justify-between">
          <div className="flex items-center gap-2">
            <Database className="h-6 w-6 text-primary" />
            <span className="font-semibold text-lg">DataGouv Dashboard Builder</span>
          </div>
          <nav className="flex items-center gap-4">
            <a
              href="https://www.data.gouv.fr"
              target="_blank"
              rel="noopener noreferrer"
              className="text-sm text-muted-foreground hover:text-foreground transition-colors"
            >
              data.gouv.fr
            </a>
            <a
              href="https://github.com"
              target="_blank"
              rel="noopener noreferrer"
              className="text-sm text-muted-foreground hover:text-foreground transition-colors"
            >
              GitHub
            </a>
          </nav>
        </div>
      </header>

      {/* Hero Section */}
      <section className="py-20 lg:py-32">
        <div className="container mx-auto px-4 text-center">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-primary/10 text-primary text-sm mb-6">
            <span>No-code dashboard builder for French open data</span>
          </div>
          <h1 className="text-4xl md:text-6xl font-bold tracking-tight mb-6">
            Turn data.gouv.fr datasets
            <br />
            <span className="text-primary">into insights instantly</span>
          </h1>
          <p className="text-lg text-muted-foreground max-w-2xl mx-auto mb-8">
            Search, analyze, and visualize open data from the French government.
            Automatic dashboard generation with transparent SQL queries.
          </p>
          <Button size="lg" className="gap-2">
            Browse Datasets
            <ArrowRight className="h-4 w-4" />
          </Button>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-20 bg-muted/50">
        <div className="container mx-auto px-4">
          <div className="grid md:grid-cols-3 gap-8">
            {features.map((feature, index) => (
              <div
                key={index}
                className="bg-background p-8 rounded-xl border hover:shadow-lg transition-shadow"
              >
                <div className="w-12 h-12 rounded-lg bg-primary/10 flex items-center justify-center text-primary mb-4">
                  {feature.icon}
                </div>
                <h3 className="text-xl font-semibold mb-2">{feature.title}</h3>
                <p className="text-muted-foreground">{feature.description}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* How It Works Section */}
      <section className="py-20">
        <div className="container mx-auto px-4">
          <h2 className="text-3xl font-bold text-center mb-12">How It Works</h2>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-8">
            {steps.map((step, index) => (
              <div key={index} className="text-center">
                <div className="w-16 h-16 rounded-full bg-primary text-primary-foreground flex items-center justify-center text-2xl font-bold mx-auto mb-4">
                  {step.number}
                </div>
                <h3 className="font-semibold mb-1">{step.title}</h3>
                <p className="text-sm text-muted-foreground">{step.description}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="border-t py-12">
        <div className="container mx-auto px-4">
          <div className="flex flex-col md:flex-row items-center justify-between gap-4">
            <div className="flex items-center gap-2 text-sm text-muted-foreground">
              <span>Powered by</span>
              <a
                href="https://www.data.gouv.fr"
                target="_blank"
                rel="noopener noreferrer"
                className="font-medium text-foreground hover:underline"
              >
                data.gouv.fr
              </a>
            </div>
            <div className="text-sm text-muted-foreground">
              Built with React, Tailwind CSS & shadcn/ui
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
}

export default App;
