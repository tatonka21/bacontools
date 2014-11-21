using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Text.RegularExpressions;
using CommandLine;
using CommandLine.Text;

namespace ImageValidator
{
    public static class MainClass
    {
        public static void Main(string[] args)
        {
            Options opts = new Options();

            CommandLine.Parser.Default.ParseArguments(args, opts);

            opts.WorkingDirectory = string.IsNullOrWhiteSpace(opts.WorkingDirectory) ? 
                Directory.GetCurrentDirectory() :
                new DirectoryInfo (opts.WorkingDirectory).FullName;

            IEnumerable<string> fileList = Directory.EnumerateFiles(
                 opts.WorkingDirectory, 
                "*.*",
                opts.RecursiveSearch ? SearchOption.AllDirectories : SearchOption.TopDirectoryOnly);

            fileList = opts.ProcessAllFiles ? fileList : fileList.Where(ImageValidator.IsValidImagePath);

            ImageValidator.Opts = opts;

            Action<string> OnFail = new Action<string>(DoNothingWithAString);
            
            OnFail += ReturnFileHandler(
                opts.DeleteOnFailure, 
                opts.RetainDirectories, 
                opts.MoveDirectory,
                opts.CopyDirectory, 
                opts.WorkingDirectory);

            if (!string.IsNullOrWhiteSpace(opts.LogFilePath))
            {
                var sw = new StreamWriter(new FileStream(new FileInfo(opts.LogFilePath).FullName, FileMode.Create));
                sw.AutoFlush = true;
                ImageValidator.CorruptedFileListOutput = sw;
            }
            if (opts.Mute) ImageValidator.ProgressReportOutput = StreamWriter.Null;

            ImageValidator.ProcessImages(fileList, OnFail);
        }

        internal static void DoNothingWithAString(string parameter)
        {
        }

        internal static Action<string> ReturnFileHandler(bool delete, bool retain, string move, string copy, string workdir)
        {
            if (delete) return DeleteFile;
            if (!String.IsNullOrWhiteSpace(move))
            {
                return retain ? MoveFileRetain(workdir, move) : MoveFile(move);
            }
            else if (!String.IsNullOrWhiteSpace(copy))
            {
                return retain ? CopyFileRetain(workdir, copy) : CopyFile(copy);
            }
            else return DoNothingWithAString;
        }

        internal static Action<string> MoveFileRetain(string workDirectory, string destination)
        {
            return (string fname) => DirectoryExtensions.PivotMoveFile(fname, workDirectory, destination);
        }

        internal static Action<string> CopyFileRetain(string workDirectory, string destination)
        {
            return (string fname) => DirectoryExtensions.PivotCopyFile(fname, workDirectory, destination);
        }

        internal static Action<string> MoveFile(string destination)
        {
            return (string fname) => DirectoryExtensions.MoveFile(fname, destination);
        }

        internal static Action<string> CopyFile(string destination)
        {
            return (string fname) => DirectoryExtensions.CopyFile(fname, destination);
        }


        internal static void DeleteFile(string fname)
        {
            if (File.Exists(fname)) File.Delete(fname);
        }
    }

   internal class Options
   {
       [Option('r', "recursive", Required = false, DefaultValue = false, HelpText = "Search in all subfolders.")]
       public bool RecursiveSearch {get; set;}

       [Option('d', "dir", Required = false, DefaultValue = null, HelpText = "Set the working directory.")]
       public string WorkingDirectory {get; set;}

       [Option('a', "all-files", Required = false, DefaultValue = false, HelpText = "Don't ignore files with non-image extensions.")]
       public bool ProcessAllFiles {get; set;}

       [Option('l', "log", Required = false, DefaultValue = null, HelpText = "Specify destination of the failed images list.")]
       public string LogFilePath {get; set;}

       [Option('v', "verbose", Required = false, DefaultValue = false, HelpText = "Specify what kind of exception occurred while reading file.")]
       public bool Verbose {get; set;}

       [Option("mute", Required = false, DefaultValue = false, HelpText = "Suppress progress notifications.")]
       public bool Mute {get; set;}

       [Option('m', "move-to", Required = false, MutuallyExclusiveSet = "move", DefaultValue = null, HelpText = "Specify directory where failed images will be moved.")]
       public string MoveDirectory {get; set; }

       [Option('c', "copy-to", Required = false, MutuallyExclusiveSet = "copy", DefaultValue = null, HelpText = "Specify directory where failed images will be copied.")]
       public string CopyDirectory {get; set; }

       [Option("delete", Required = false, MutuallyExclusiveSet = "delete", DefaultValue = false, HelpText = "Delete all failed images.")]
       public bool DeleteOnFailure {get; set; }

       [Option("progress-step", Required = false, DefaultValue = 100, HelpText = "Specify period of progress notifications.")]
       public int LogPeriod { get; set; }

       [Option("retain-folders", Required = false, DefaultValue = false, HelpText = "Keep directory structure when copying/moving instead of dumping all files to a single directory.")]
       public bool RetainDirectories { get; set; } // Default behavior used to be true

       [HelpOption]
       public string GetHelp()
       {
           var help = new HelpText { AddDashesToOption = true };
           help.AddOptions(this);
           return help;
       }
   }
}
