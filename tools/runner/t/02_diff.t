use Test::Most      tests => 8;
use Runner101::Diff qw(run_diff parse);


my $diffs = [];

is parse('',             $diffs), undef, 'Empty string is not parsed';
is parse('Some message', $diffs), undef, 'Regular message is not parsed';
is parse('123 W Street', $diffs), undef, 'Invalid operation is not parsed';
is_deeply                $diffs,  [],    'No diffs were gathered';


my @diff1 = ('A somefile', 'M someotherfile', 'D yetanotherfile');
my @diff2 = (@diff1, @diff1);

is run_diff(['perl', '-pe', '++$i; $_ = "$i $_"'], \@diff1, \*STDOUT, 1), 0,
                                         'successful run returns exit code 0';
is_deeply \@diff1, \@diff2,              'diff result is correct';

ok run_diff(['false'], [], \*STDOUT, 0), 'failing run returns non-zero';

dies_ok {
    local $SIG{__WARN__} = sub { die @_ };
    run_diff([], [], \*STDOUT, 1);
} 'invalid command causes warning';
