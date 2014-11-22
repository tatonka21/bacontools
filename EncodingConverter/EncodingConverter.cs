using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using CommandLine;
using CommandLine.Parsing;
using System.IO;

namespace EncodingConverter
{
    public static class EncodingConverter
    {
        public static void Main(string[] args)
        {
            var opts = new Options();
            var p = new CommandLine.Parser();
            p.ParseArguments(args, opts);

            IEnumerable<string> files = Directory.EnumerateFiles(Directory.GetCurrentDirectory(),
                opts.FilePattern, opts.Recursive ? SearchOption.AllDirectories : SearchOption.TopDirectoryOnly);

            foreach (string s in files)
            {
                Encoding f = Encoding.GetEncoding(opts.SourceEncoding);
                Encoding t = Encoding.GetEncoding(opts.TargetEncoding);

                File.WriteAllBytes(s, Encoding.Convert(f, t, File.ReadAllBytes(s)));
            }
        }
    }

    internal class Options
    {
        [Option('f', "from", Required = true, HelpText = "Source encoding.")]
        public string SourceEncoding {get; set; }

        [Option('t', "to", Required = true, HelpText = "Target encoding.")]
        public string TargetEncoding { get; set; }

        [Option('f', "file", Required = true, HelpText = "Input file(s).")]
        public string FilePattern { get; set; }

        [Option('r', "recursive", Required = false, DefaultValue = false, HelpText = "Search in subdirectories.")]
        public bool Recursive { get; set; }
    }
}