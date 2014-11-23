using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using CommandLine;
using CommandLine.Parsing;
using CommandLine.Text;
using System.IO;
using System.Diagnostics;

namespace EncodingConverter
{
    public static class EncodingConverter
    {
        public static void Main(string[] args)
        {
            Encoding f = Encoding.UTF8;
            Encoding t = Encoding.UTF8;
            IEnumerable<string> files = Enumerable.Empty<string>();
            var opts = new Options();
            Stopwatch sw = new Stopwatch();
            Parser.Default.ParseArgumentsStrict(args, opts, () => 
            {
                if (!(args.Select(s => s.Trim()).Contains(@"-?") 
                    || args.Select(s => s.Trim()).Contains(@"--help")
                    || args.Select(s => s.Trim()).Contains(@"-help")))
                    Console.WriteLine("Invalid input. Call {0} --help for option syntax.", Process.GetCurrentProcess().ProcessName);
                Environment.Exit(1);
            });

            if (opts.ListEncodings)
            {
                Console.WriteLine("Available encodings: ");
                foreach (var ei in Encoding.GetEncodings()) Console.Write("{0} ", ei.Name);
                Console.WriteLine();
                Environment.Exit(1);
            }

            try
            {
                files = Directory.EnumerateFiles(Directory.GetCurrentDirectory(),
                    opts.FilePattern, opts.Recursive ? SearchOption.AllDirectories : SearchOption.TopDirectoryOnly);
                Console.WriteLine("Files to be converted: {0}", files.Count());
            }
            catch (DirectoryNotFoundException e)
            {
                Console.WriteLine("Unrecognized file pattern: {0}", opts.FilePattern);
                Environment.Exit(1);
            }

            try
            {
                f = Encoding.GetEncoding(opts.SourceEncoding);
            }
            catch (ArgumentException e)
            {
                Console.WriteLine("Unrecognized source encoding: {0}", opts.SourceEncoding);
                Environment.Exit(1);
            }

            try
            {
                t = Encoding.GetEncoding(opts.TargetEncoding);
            }
            catch (ArgumentException e)
            {
                Console.WriteLine("Unrecognized target encoding: {0}", opts.TargetEncoding);
                Environment.Exit(1);
            }

            sw.Restart();
            files.AsParallel().ForAll(s => File.WriteAllBytes(s, Encoding.Convert(f, t, File.ReadAllBytes(s))));
            sw.Stop();
            Console.WriteLine("Conversion completed in {0} ms.", sw.ElapsedMilliseconds);
        }
    }

    internal class Options
    {
        [Option('f', "from", Required = false, DefaultValue = @"utf-8", HelpText = "Source encoding.", MutuallyExclusiveSet = "convert")]
        public string SourceEncoding {get; set; }

        [Option('t', "to", Required = false, DefaultValue = @"utf-8", HelpText = "Target encoding.", MutuallyExclusiveSet = "convert")]
        public string TargetEncoding { get; set; }

        [Option('p', "pattern", Required = false, DefaultValue = @"*.txt", HelpText = "Input file pattern.", MutuallyExclusiveSet = "convert")]
        public string FilePattern { get; set; }

        [Option('r', "recursive", Required = false, DefaultValue = false, HelpText = "Search in subdirectories.", MutuallyExclusiveSet = "convert")]
        public bool Recursive { get; set; }

        [Option('l', "list-encodings", Required = false, DefaultValue = false, HelpText = "List all available encodings.", MutuallyExclusiveSet = "help")]
        public bool ListEncodings { get; set; }

        [HelpOption('?', "help", MutuallyExclusiveSet = "help")]
        public string GetHelp()
        {
            var help = new HelpText { AddDashesToOption = true };
            help.AddOptions(this);
            return help;
        }
    }
}